"""Read-only native document/evidence validation. No learner apps or network calls."""
from pathlib import Path
from datetime import datetime, timezone
import argparse
import ast
import copy
import json
import re
import sys
import ntpath
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
STEPS = {
    '0.3': ('execution', 'explanation'), '0.4': ('execution', 'explanation'),
    '0.5': ('modification', 'explanation'), '0.6': ('execution', 'explanation'),
    '0.7': ('execution', 'explanation'), '0.8': ('execution', 'debug'),
    '0.9': ('modification', 'explanation', 'transfer'),
    'J1': ('execution', 'explanation', 'debug'),
    'J2': ('modification', 'explanation', 'transfer'),
    'J3': ('execution', 'explanation', 'debug'),
    'J4': ('execution', 'explanation', 'debug'),
    'J5': ('execution', 'explanation', 'modification', 'debug', 'transfer'),
}
LATER = [f'Q{i}' for i in range(5, 13)]
KINDS = {'execution', 'explanation', 'modification', 'debug', 'transfer', 'engagement', 'operational', 'location'}
ASSISTANCE = {'none', 'docs', 'hint', 'scaffold', 'worked_example', 'ai_implemented'}
STATUSES = {'not_started', 'introduced', 'practiced', 'applied_independently', 'production_understanding'}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def timestamp(value):
    require(isinstance(value, str), 'date/timestamp must be text')
    result = datetime.fromisoformat(value.replace('Z', '+00:00'))
    return result.replace(tzinfo=timezone.utc) if result.tzinfo is None else result.astimezone(timezone.utc)


def nonempty(value):
    return isinstance(value, str) and bool(value.strip())


def local_ref(root, value):
    require(nonempty(value), 'empty evidence/source reference')
    if value.startswith(('conversation:', 'turn:', 'https://', 'http://')):
        require(nonempty(value.split(':', 1)[1].strip('/')), 'empty source identifier')
        return
    path = Path(value)
    require(not path.is_absolute() and not re.match(r'^[A-Za-z]:', value), 'source artifact must be repository-relative')
    resolved = (root / path).resolve()
    require(resolved.is_relative_to(root.resolve()), 'source path escapes repository')
    require(resolved.is_file(), f'missing source artifact: {value}')


def validate_state(current, skills, events, root=None):
    """Raise ValueError for an incoherent candidate checkpoint; return True otherwise."""
    require(isinstance(current, dict) and isinstance(skills, dict), 'snapshots must be objects')
    for name in ('conceptual_thread', 'expected_evidence', 'pending_action'):
        require(nonempty(current.get(name)), f'missing resume context: {name}')
    for name in ('blocker', 'next_retrieval_target', 'active_minutes_observed'):
        require(name in current, f'missing resume context: {name}')
    for name in ('blocker', 'next_retrieval_target'):
        require(current[name] is None or nonempty(current[name]), f'invalid {name}')
    require(current.get('assistance_level') in ASSISTANCE, 'missing/invalid assistance')
    onboarding = current.get('onboarding')
    require(isinstance(onboarding, dict) and all(nonempty(onboarding.get(k)) for k in ('status', 'calibration', 'source'))
            and type(onboarding.get('runtime_proof')) is bool, 'invalid onboarding context')
    provider = current.get('provider')
    require(isinstance(provider, dict) and all(nonempty(provider.get(k)) for k in ('name', 'reference', 'baseline_date'))
            and isinstance(provider.get('installed_versions'), dict), 'invalid provider context')
    timestamp(provider['baseline_date'])
    require(all(v is None or nonempty(v) for v in provider['installed_versions'].values()), 'invalid installed versions')
    if root:
        local_ref(root, onboarding['source']); local_ref(root, provider['reference'])
    require(type(current.get('schema_version')) is int and current['schema_version'] == 1, 'current schema version')
    require(type(skills.get('schema_version')) is int and skills['schema_version'] == 1, 'skills schema version')
    require(current.get('mode') in {'learn', 'assess', 'build_together'}, 'unknown teaching mode')
    require(current.get('route') == 'J0-J5', 'unknown initial route')
    rows = skills['skills'] + skills['later_modules']
    ids = [row['id'] for row in rows]
    require(len(ids) == len(set(ids)), 'duplicate skill ID')
    require(set(ids) == {f'E{i:02}' for i in range(1, 23)} | set(LATER), 'missing/unknown skill IDs')
    require(isinstance(events, list) and events, 'empty evidence log')
    require(events[0].get('kind') == 'initialization' and events[0].get('actor') == 'maintainer', 'first event must initialize')
    records, invalid = {}, set()
    previous = datetime.min.replace(tzinfo=timezone.utc)
    for event in events:
        eid = event.get('id')
        require(nonempty(eid) and eid not in records, 'empty/duplicate evidence ID')
        when = timestamp(event['at'])
        require(when >= previous, 'evidence chronological ordering')
        previous = when
        kind = event.get('kind')
        if kind == 'initialization':
            require(not records and event.get('actor') == 'maintainer' and nonempty(event.get('summary')), 'invalid initialization')
        elif kind == 'correction':
            old = event.get('supersedes')
            require(event.get('actor') == 'maintainer' and nonempty(event.get('reason')), 'invalid correction')
            require(old in records and records[old].get('actor') == 'learner' and old not in invalid, 'correction target must be an active earlier learner event')
            invalid.add(old)
        else:
            require(kind in KINDS and event.get('actor') == 'learner', 'invalid learner kind/actor')
            require(event.get('milestone') in set(STEPS) | set(LATER), 'unknown evidence milestone')
            require(event.get('outcome') in {'pass', 'fail', 'observed'}, 'invalid outcome')
            require(event.get('assistance') in ASSISTANCE, 'unknown assistance level')
            require(isinstance(event.get('skill_ids'), list) and set(event['skill_ids']) <= set(ids), 'unknown evidence skill')
            require(len(event['skill_ids']) == len(set(event['skill_ids'])), 'duplicate evidence skill')
            require(nonempty(event.get('expected')) and nonempty(event.get('observation')), 'expected/observation missing')
            require(nonempty(event.get('source')), 'traceable evidence source missing')
            require(isinstance(event.get('redactions'), list) and all(nonempty(x) for x in event['redactions']), 'invalid redactions')
            if kind == 'location':
                require(nonempty(event.get('observed_path')), 'location evidence needs observed_path')
        if root and kind != 'correction':
            local_ref(root, event['source'])
        records[eid] = event
    require(current.get('last_event_id') == events[-1]['id'], 'snapshot/log last_event_id mismatch')
    require(timestamp(current['updated_at']) >= previous, 'snapshot date precedes evidence')
    require(skills.get('last_event_id') == events[-1]['id'], 'skills snapshot/log revision mismatch')
    require(timestamp(skills['updated_at']) >= previous, 'skills snapshot date precedes evidence')
    learner = [e for e in events if e.get('actor') == 'learner']
    require(current.get('last_learner_event') == (learner[-1]['id'] if learner else None), 'last learner event mismatch')
    latest, latest_skill = {}, {}
    for event in learner:
        if event['id'] not in invalid:
            latest[event['milestone'], event['kind']] = event['id']
            for sid in event['skill_ids']:
                latest_skill[sid, event['milestone'], event['kind']] = event['id']

    def references(evidence_ids, skill=None):
        require(isinstance(evidence_ids, list) and len(evidence_ids) == len(set(evidence_ids)), 'invalid evidence reference list')
        found = []
        for eid in evidence_ids:
            require(eid in records, f'missing evidence ID: {eid}')
            event = records[eid]
            require(eid not in invalid and event.get('actor') == 'learner', 'invalidated/non-learner evidence cannot support status')
            fresh = latest_skill.get((skill, event['milestone'], event['kind'])) if skill else latest.get((event['milestone'], event['kind']))
            require(fresh == eid, 'stale evidence cannot support status')
            if skill:
                require(skill in event['skill_ids'], 'evidence does not support this skill')
            found.append(event)
        return found

    milestones = current['milestones']
    mids = [m['id'] for m in milestones]
    require(len(mids) == len(set(mids)) and set(STEPS) <= set(mids), 'missing/duplicate milestones')
    require(set(mids) <= set(STEPS) | set(LATER), 'unknown milestone')
    by_id = {m['id']: m for m in milestones}
    for m in milestones:
        mid = m['id']
        stage = 'J0' if mid.startswith('0.') else mid
        require(m.get('stage') == stage, 'milestone stage mismatch')
        required = set(STEPS.get(mid, ('execution', 'explanation', 'debug')))
        require(set(m['gates']) == required, 'missing/unknown required gates')
        require(m.get('status') in {'pending', 'in_progress', 'complete'}, 'invalid milestone status')
        for kind, gate in m['gates'].items():
            require(gate.get('status') in {'pending', 'satisfied'}, 'invalid gate status')
            evidence = references(gate['evidence_ids'])
            require(all(e['kind'] == kind and e['milestone'] == mid for e in evidence), 'gate evidence kind/milestone mismatch')
            if gate['status'] == 'satisfied':
                require(evidence and all(e['outcome'] == 'pass' for e in evidence), 'satisfied gate needs current passing evidence')
                if kind in {'explanation', 'modification', 'debug', 'transfer'}:
                    require(all(e['assistance'] != 'ai_implemented' for e in evidence), 'ownership gate requires learner work')
                if kind == 'transfer':
                    practice = references(m['gates']['modification']['evidence_ids'])
                    require(any(p['outcome'] == 'pass' and timestamp(t['at']).date() > timestamp(p['at']).date()
                                for t in evidence for p in practice), 'milestone transfer must follow modification on a later date')
        if m['status'] == 'complete':
            require(all(g['status'] == 'satisfied' for g in m['gates'].values()), 'complete milestone has unsatisfied gates')
    active = current.get('milestone')
    require(active in by_id, 'unknown active milestone')
    active_stage = by_id[active]['stage']
    require(current.get('stage') == active_stage and current.get('quest') == ('Q0' if active_stage == 'J0' else active_stage), 'active stage/quest mismatch')
    order = list(STEPS)
    for mid, m in by_id.items():
        predecessors = order[:order.index(mid)] if mid in order else order
        if mid == active:
            require(all(by_id[p]['status'] == 'complete' for p in predecessors), 'incomplete milestone prerequisite')
        elif m['status'] != 'pending':
            # Reopened prerequisites do not erase work demonstrated after an earlier pass.
            own = [e for e in learner if e['milestone'] == mid]
            started = min((timestamp(e['at']) for e in own), default=previous)
            for p in predecessors:
                if by_id[p]['status'] == 'complete':
                    continue
                history = [e for e in learner if e['milestone'] == p and e['outcome'] == 'pass'
                           and timestamp(e['at']) <= started and e['assistance'] != 'ai_implemented']
                require(set(STEPS[p]) <= {e['kind'] for e in history}, 'downstream history lacks earlier prerequisite evidence')
    for row in rows:
        status = row['status']
        require(status in STATUSES, 'unknown skill status')
        evidence = references(row['evidence_ids'], row['id'])
        if status == 'not_started':
            continue
        passing = [e for e in evidence if e['outcome'] == 'pass']
        kinds = {e['kind'] for e in passing}
        if status == 'introduced':
            require(bool(kinds & {'engagement', 'explanation'}), 'introduced skill lacks learner engagement/explanation')
        elif status == 'practiced':
            require(bool(kinds & {'execution', 'modification', 'debug', 'transfer'}), 'practiced skill lacks practice')
        else:
            independent = [e for e in passing if e['assistance'] in {'none', 'docs'}]
            require({'explanation', 'modification', 'debug', 'transfer'} <= {e['kind'] for e in independent}, 'independent skill lacks independent evidence')
            require(any(timestamp(t['at']).date() > timestamp(p['at']).date()
                        for t in independent if t['kind'] == 'transfer'
                        for p in independent if p['kind'] == 'modification'), 'independent transfer must follow practice on a later date')
            if status == 'production_understanding':
                require('operational' in {e['kind'] for e in independent}, 'production status lacks operational evidence')
    queues = skills['review_queues']
    require(set(queues) == {'blockers', 'delayed_practice', 'role_gaps'}, 'review queue keys')
    for entries in queues.values():
        require(isinstance(entries, list), 'review queue must be list')
        for entry in entries:
            references(entry['evidence_ids'])
            require(entry['evidence_ids'] and all(nonempty(entry.get(k)) for k in ('observation', 'next_task', 'trigger')), 'review queue lacks observation/task/trigger')
    location = current['code_location']
    require(location['status'] in {'unverified', 'verified'}, 'location status')
    require(location['path'] is None or nonempty(location['path']), 'location path')
    if location['status'] == 'verified':
        require(nonempty(location['path']), 'verified location needs path')
        evidence = references([location['evidence_id']])
        require(evidence[0]['kind'] == 'location' and evidence[0]['outcome'] == 'pass'
                and ntpath.normcase(ntpath.normpath(location['path'])) == ntpath.normcase(ntpath.normpath(evidence[0]['observed_path'])), 'verified location needs matching observed path')
    require(nonempty(current.get('pending_action')), 'pending action missing')
    minutes = current.get('active_minutes_observed')
    require(minutes is None or (type(minutes) in (int, float) and minutes >= 0), 'invalid observed active time')
    return True


def read_state(root):
    current = json.loads((root/'progress/current.json').read_text(encoding='utf-8'))
    skills = json.loads((root/'progress/skills.json').read_text(encoding='utf-8'))
    lines = (root/'progress/evidence.jsonl').read_text(encoding='utf-8').splitlines()
    require(all(line.strip() for line in lines), 'blank evidence line')
    return current, skills, [json.loads(line) for line in lines]


def anchors(body):
    result, seen, fenced = set(), {}, False
    for line in body.splitlines():
        if line.strip().startswith('```'):
            fenced = not fenced
        if not fenced and re.match(r'^#{1,6}\s+', line):
            heading = re.sub(r'^#{1,6}\s+', '', line).strip().rstrip('#').strip().lower()
            slug = re.sub(r'[^\w\s-]', '', heading).replace(' ', '-')
            count = seen.get(slug, 0); seen[slug] = count + 1
            result.add(slug if not count else f'{slug}-{count}')
    return result


def frontmatter(body):
    match = re.match(r'\A---\r?\n(.*?)\r?\n---(?:\r?\n|$)', body, re.S)
    require(match is not None, 'SPEC.md: missing/malformed front matter')
    return match.group(1)


def check_link(path, link):
    if link.startswith(('https://', 'http://')):
        return
    name, _, fragment = link.partition('#')
    target = (path.parent / unquote(name)).resolve() if name else path
    require(target.exists(), f'broken link: {path.name}: {link}')
    if fragment and target.suffix.lower() == '.md':
        require(unquote(fragment) in anchors(target.read_text(encoding='utf-8')), f'broken anchor: {path.name}: {link}')


def validate_documents(root):
    required = ['AGENTS.md', 'AGENT.md', 'README.md', '.agents/skills/ai-engineering-tutor/SKILL.md',
                'docs/CURRICULUM.md', 'docs/TEACHING_GUIDE.md', 'docs/ENGINEERING_GUIDE.md',
                'docs/PROGRESS_PROTOCOL.md', 'docs/PORTFOLIO.md', 'docs/PROVIDER_REFERENCE.md',
                'docs/PILOT.md', 'docs/MIGRATION.md', '_bmad-output/specs/spec-codex-learning-workspace/SPEC.md']
    for name in required:
        require((root/name).is_file(), f'missing owned file: {name}')
    files = [root/n for n in required] + list((root/'docs').glob('*.md')) + list((root/'_bmad-output/specs').rglob('*.md'))
    for path in set(files):
        body = path.read_text(encoding='utf-8')
        require(sum(line.strip().startswith('```') for line in body.splitlines()) % 2 == 0, f'unbalanced fence: {path.name}')
        for link in re.findall(r'(?<!!)\[[^\]\n]+\]\(([^)\n]+)\)', body):
            check_link(path, link)
    spec = root/'_bmad-output/specs/spec-codex-learning-workspace/SPEC.md'
    front = frontmatter(spec.read_text(encoding='utf-8'))
    for name in re.findall(r'^  - (.+)$', front, re.M):
        require((spec.parent/name.strip()).is_file(), f'missing spec companion: {name}')
    provider = (root/'docs/PROVIDER_REFERENCE.md').read_text(encoding='utf-8')
    blocks = re.findall(r'```python\n(.*?)\n```', provider, re.S)
    require(blocks, 'provider code reference missing')
    for block in blocks:
        ast.parse(block)
    return len(set(files))


def self_test(root):
    fixture = json.loads((root/'tools/fixtures/initial_checkpoint.json').read_text(encoding='utf-8'))
    # Use frozen synthetic initial state, independent of legitimate live progress.
    c, s, events = copy.deepcopy((fixture['current'], fixture['skills'], fixture['events']))
    count = 0
    def test(label, candidate, accepted):
        nonlocal count
        try:
            validate_state(*candidate, root=root)
            actual = True
        except (ValueError, KeyError, TypeError):
            actual = False
        require(actual == accepted, f'self-test mismatch: {label}')
        count += 1
    test('initial pending', (c,s,events), True)
    def event(kind, eid, outcome='pass', day='2026-09-08', assistance='docs'):
        return {'id':eid, 'at':day, 'kind':kind, 'actor':'learner', 'milestone':'0.3', 'skill_ids':['E03'],
                'outcome':outcome, 'assistance':assistance, 'expected':'Synthetic fixture expectation',
                'observation':'Synthetic fixture only', 'source':'conversation:fixture', 'redactions':[]}
    def append(candidate, item):
        a,b,e = candidate
        e.append(item); a['last_event_id']=item['id']; a['updated_at']=item['at']
        b['last_event_id']=item['id']; b['updated_at']=item['at']
        if item['actor']=='learner': a['last_learner_event']=item['id']
    execution = copy.deepcopy((c,s,events)); append(execution,event('execution','run'))
    execution[0]['milestones'][0]['gates']['execution']={'status':'satisfied','evidence_ids':['run']}
    test('valid execution only, no forced advancement', execution, True)
    bad=copy.deepcopy(execution); bad[0]['milestones'][0]['status']='complete'; test('execution cannot complete',bad,False)
    complete=copy.deepcopy(execution); append(complete,event('explanation','explain'))
    complete[0]['milestones'][0]['gates']['explanation']={'status':'satisfied','evidence_ids':['explain']}
    complete[0]['milestones'][0]['status']='complete'; test('valid completion',complete,True)
    advance=copy.deepcopy(complete); advance[0]['milestone']='0.4'; advance[0]['milestones'][1]['status']='in_progress'; test('valid later milestone',advance,True)
    bad=copy.deepcopy(execution); bad[0]['milestone']='J1'; bad[0]['stage']='J1'; bad[0]['quest']='J1'; test('cannot skip prerequisites',bad,False)
    bad=copy.deepcopy(complete); bad[0]['milestones'][0]['gates']['explanation']['evidence_ids']=['run']; test('wrong-kind evidence',bad,False)
    bad=copy.deepcopy(complete); del bad[0]['milestones'][0]['gates']['explanation']; test('cannot remove required gate',bad,False)
    bad=copy.deepcopy(complete); append(bad,event('execution','newfail','fail')); test('newer failure defeats pass',bad,False)
    bad=copy.deepcopy(complete); append(bad,{'id':'correction','at':'2026-09-08','kind':'correction','actor':'maintainer','supersedes':'run','reason':'Wrong output'}); test('correction invalidates evidence',bad,False)
    bad=copy.deepcopy(complete); bad[0]['last_event_id']='run'; test('partial checkpoint',bad,False)
    bad=copy.deepcopy(complete); bad[2].append(copy.deepcopy(bad[2][-1])); test('duplicate event',bad,False)
    bad=copy.deepcopy(complete); bad[0]['milestones'][0]['gates']['execution']['evidence_ids']=['missing']; test('missing reference',bad,False)
    practiced=copy.deepcopy(execution); practiced[1]['skills'][2].update(status='practiced',evidence_ids=['run']); test('legitimate skill progress',practiced,True)
    bad=copy.deepcopy(practiced); bad[1]['skills'][2]['status']='applied_independently'; test('execution is not independence',bad,False)
    independent=copy.deepcopy(complete)
    for kind,day in [('modification','2026-09-08'),('debug','2026-09-08'),('transfer','2026-09-09')]: append(independent,event(kind,kind,day=day))
    independent[1]['skills'][2].update(status='applied_independently',evidence_ids=['explain','modification','debug','transfer'])
    test('independent delayed evidence',independent,True)
    bad=copy.deepcopy(independent); bad[2][-1]['assistance']='ai_implemented'; test('AI-written transfer not independent',bad,False)
    bad=copy.deepcopy(independent); bad[2][-1]['at']='2026-09-08'; test('transfer needs delay',bad,False)
    bad=copy.deepcopy(independent); bad[1]['skills'][2]['status']='production_understanding'; test('operational evidence required',bad,False)
    bad=copy.deepcopy((c,s,events)); bad[0]['code_location'].update(path='C:/example/app',status='verified',evidence_id='init-20260908'); test('no invented code location',bad,False)
    bad=copy.deepcopy(complete); bad[1]['last_event_id']='init-20260908'; test('partial skills save',bad,False)
    for field in ('onboarding','provider','conceptual_thread','expected_evidence','assistance_level','blocker','next_retrieval_target'):
        bad=copy.deepcopy(complete); del bad[0][field]; test('missing '+field,bad,False)
    for source, valid in [('README.md',True),('missing-evidence-file.txt',False),('../outside.txt',False),('C:/outside.txt',False),('conversation:',False),('turn:',False)]:
        bad=copy.deepcopy(complete); bad[2][-1]['source']=source; test('source '+source,bad,valid)
    bad=copy.deepcopy(complete); bad[2][-1]['assistance']='ai_implemented'; test('AI explanation gate',bad,False)
    scoped=copy.deepcopy(practiced); other=event('execution','other'); other['skill_ids']=['E01']; append(scoped,other)
    scoped[0]['milestones'][0]['gates']['execution']['evidence_ids']=['other']; test('unrelated skill evidence remains valid',scoped,True)
    located=copy.deepcopy((c,s,events)); item=event('location','loc'); item['observed_path']='C:/example/app'; append(located,item)
    located[0]['code_location'].update(path='c:\\example\\app',status='verified',evidence_id='loc'); test('exact normalized location',located,True)
    bad=copy.deepcopy(located); bad[2][-1]['observed_path']='C:/example/app-backup'; test('substring location rejected',bad,False)
    regression=copy.deepcopy(advance); append(regression,event('execution','regression','fail'))
    regression[0]['milestone']='0.3'; regression[0]['milestones'][0]['status']='in_progress'
    regression[0]['milestones'][0]['gates']['execution']={'status':'pending','evidence_ids':['regression']}
    test('reassessment preserves downstream history',regression,True)
    delayed=copy.deepcopy((c,s,events)); target=delayed[0]['milestones'][6]
    for kind in ('modification','explanation','transfer'):
        item=event(kind,'delay-'+kind); item['milestone']='0.9'; append(delayed,item)
        target['gates'][kind]={'status':'satisfied','evidence_ids':[item['id']]}
    test('same day milestone transfer',delayed,False)
    delayed[2][-1]['at']='2026-09-09'; delayed[0]['updated_at']=delayed[1]['updated_at']='2026-09-09'; test('later milestone transfer',delayed,True)
    def document_test(label, operation, accepted):
        nonlocal count
        try:
            operation(); actual=True
        except ValueError:
            actual=False
        require(actual == accepted, f'self-test mismatch: {label}'); count += 1
    document_test('valid front matter', lambda: frontmatter('---\nid: fixture\n---\n'), True)
    document_test('malformed front matter', lambda: frontmatter('# no front matter'), False)
    document_test('valid anchor', lambda: check_link(root/'AGENTS.md','#learning-workspace'), True)
    document_test('broken anchor', lambda: check_link(root/'AGENTS.md','#missing-fixture-heading'), False)
    return count


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--self-test',action='store_true')
    parser.add_argument('--root',type=Path,default=ROOT)
    args=parser.parse_args()
    try:
        root=args.root.resolve()
        validate_state(*read_state(root),root=root)
        documents=validate_documents(root)
        print(f'PASS: native state, evidence relationships and {documents} owned documents')
        if args.self_test: print(f'PASS: {self_test(root)} in-memory positive/negative fixtures')
        print('Read-only static validation. Learner execution, understanding and teaching effectiveness are not established.')
    except (ValueError, KeyError, TypeError, AttributeError, OSError, SyntaxError) as exc:
        print(f'FAIL: {exc}',file=sys.stderr)
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())
