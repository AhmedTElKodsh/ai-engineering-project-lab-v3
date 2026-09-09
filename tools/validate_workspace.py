"""Read-only native document/evidence validation. No learner apps or network calls."""
from pathlib import Path
from datetime import datetime, timezone, timedelta
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
    'J1': ('execution', 'explanation', 'modification', 'debug'),
    'J2': ('modification', 'explanation', 'transfer'),
    'J3': ('execution', 'explanation', 'modification', 'debug'),
    'J4': ('execution', 'explanation', 'modification', 'debug'),
    'J5': ('execution', 'explanation', 'modification', 'debug', 'transfer'),
}
LATER = [f'Q{i}' for i in range(5, 13)]
# Inherited J0 setup milestones. Ungated by design, but a genuine prerequisite failure
# must have a legal home rather than being relabeled under 0.3.
PRE_STEPS = ('0.1', '0.2')
KINDS = {'execution', 'explanation', 'modification', 'debug', 'transfer', 'engagement', 'operational', 'location'}
ASSISTANCE = {'none', 'docs', 'hint', 'scaffold', 'worked_example', 'ai_implemented'}
STATUSES = {'not_started', 'introduced', 'practiced', 'applied_independently', 'production_understanding'}
PROVIDER_VERSION_KEYS = {'python', 'uv', 'groq', 'python-dotenv'}
ENTRY_PREREQUISITES = {
    '0.3': (), '0.4': ('0.3',), '0.5': ('0.4',), '0.6': ('0.5',),
    '0.7': ('0.6',), '0.8': ('0.7',), '0.9': ('0.8',),
    'J1': ('0.9',), 'J2': ('J1',), 'J3': ('J2',),
    # Direct SQL and a scoped read tool can begin after J2. Retrieval joins the
    # dependency set before the combined policy/order workflow can complete.
    'J4': ('J2',), 'J5': ('J4',),
}
COMPLETION_PREREQUISITES = {**ENTRY_PREREQUISITES, 'J4': ('J2', 'J3')}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def timestamp(value):
    require(isinstance(value, str) and re.fullmatch(r'\d{4}-\d{2}-\d{2}(?:T\d{2}:\d{2}:\d{2}(?:\.\d+)?(?:Z|[+-]\d{2}:\d{2})?)?', value), 'date/timestamp must be canonical date or full ISO timestamp')
    result = datetime.fromisoformat(value.replace('Z', '+00:00'))
    return result.replace(tzinfo=timezone.utc) if result.tzinfo is None else result.astimezone(timezone.utc)


def delayed_after(transfer, practice):
    """Date-only evidence has unknown time: demand a full intervening day."""
    later, earlier = timestamp(transfer), timestamp(practice)
    if len(transfer) == 10 or len(practice) == 10:
        return (later.date() - earlier.date()).days >= 2
    return later - earlier >= timedelta(days=1)


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
    require(set(provider['installed_versions']) == PROVIDER_VERSION_KEYS, 'installed version keys must be exactly python, uv, groq and python-dotenv')
    timestamp(provider['baseline_date'])
    require(all(v is None or nonempty(v) for v in provider['installed_versions'].values()), 'invalid installed versions')
    if root:
        local_ref(root, onboarding['source']); local_ref(root, provider['reference'])
    require(type(current.get('schema_version')) is int and current['schema_version'] == 1, 'current schema version')
    require(type(skills.get('schema_version')) is int and skills['schema_version'] == 1, 'skills schema version')
    require(current.get('mode') in {'learn', 'assess', 'build_together'}, 'unknown teaching mode')
    require(current.get('route') == 'J0-J5', 'unknown initial route')
    require(all(isinstance(skills.get(k), list) and all(isinstance(r, dict) for r in skills[k]) for k in ('skills', 'later_modules')), 'skill rows must be objects')
    initial_ids = {f'E{i:02}' for i in range(1, 23)}
    require({r.get('id') for r in skills['skills']} == initial_ids and {r.get('id') for r in skills['later_modules']} == set(LATER), 'skill partition mismatch')
    rows = skills['skills'] + skills['later_modules']
    ids = [row['id'] for row in rows]
    require(len(ids) == len(set(ids)), 'duplicate skill ID')
    require(set(ids) == {f'E{i:02}' for i in range(1, 23)} | set(LATER), 'missing/unknown skill IDs')
    require(isinstance(events, list) and events, 'empty evidence log')
    require(all(isinstance(e, dict) for e in events), 'evidence events must be objects')
    require(events[0].get('kind') == 'initialization' and events[0].get('actor') == 'maintainer', 'first event must initialize')
    records, invalid = {}, set()

    def scopes_overlap(first, second):
        """Empty tags are milestone-wide; otherwise overlap needs a shared capability."""
        left, right = set(first.get('skill_ids', [])), set(second.get('skill_ids', []))
        return not left or not right or bool(left & right)

    def is_fresh(candidate, observations):
        position = observations.index(candidate)
        return not any(other.get('actor') == 'learner' and other.get('id') not in invalid
                       and other.get('milestone') == candidate.get('milestone')
                       and other.get('kind') == candidate.get('kind')
                       and scopes_overlap(candidate, other)
                       for other in observations[position + 1:])
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
        elif kind == 'readiness':
            mid = event.get('milestone')
            require(event.get('actor') == 'maintainer' and mid in STEPS and 'transfer' in STEPS[mid], 'invalid readiness decision')
            require(all(nonempty(event.get(k)) for k in ('source', 'eligible_after', 'next_task', 'trigger')), 'readiness decision lacks review contract')
            refs = event.get('evidence_ids')
            require(isinstance(refs, list) and all(isinstance(e, str) for e in refs) and len(refs) == len(set(refs)), 'invalid readiness references')
            prior = list(records.values())
            proof = [records[eid] for eid in refs if eid in records]
            needed = set(STEPS[mid]) - {'transfer'}
            require(len(proof) == len(refs) and {e['kind'] for e in proof} == needed
                    and all(e.get('actor') == 'learner' and e['milestone'] == mid and e['id'] not in invalid
                            and is_fresh(e, prior) for e in proof), 'readiness needs then-current non-transfer evidence')
            require(all(e['outcome'] == 'pass' and (e['kind'] == 'execution' or e['assistance'] != 'ai_implemented')
                        and (mid != 'J5' or e['kind'] == 'execution' or e['assistance'] in {'none', 'docs'})
                        for e in proof), 'readiness requires passing ownership evidence')
            modification = next(e for e in proof if e['kind'] == 'modification')
            require(delayed_after(event['eligible_after'], modification['at']), 'readiness review is premature')
        elif kind == 'correction':
            old = event.get('supersedes')
            require(event.get('actor') == 'maintainer' and nonempty(event.get('reason')), 'invalid correction')
            require(old in records and records[old].get('actor') == 'learner' and old not in invalid, 'correction target must be an active earlier learner event')
            invalid.add(old)
        else:
            require(kind in KINDS and event.get('actor') == 'learner', 'invalid learner kind/actor')
            require(event.get('milestone') in set(STEPS) | set(LATER) | set(PRE_STEPS), 'unknown evidence milestone')
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
    def references(evidence_ids, skill=None):
        require(isinstance(evidence_ids, list) and len(evidence_ids) == len(set(evidence_ids)), 'invalid evidence reference list')
        found = []
        for eid in evidence_ids:
            require(eid in records, f'missing evidence ID: {eid}')
            event = records[eid]
            require(eid not in invalid and event.get('actor') == 'learner', 'invalidated/non-learner evidence cannot support status')
            # Their capability-scoped freshness decides staleness; the message names the
            # repair, because a newer honest observation is the usual cause, not corruption.
            newer = None if is_fresh(event, events) else next(
                (o['id'] for o in events[events.index(event) + 1:]
                 if o.get('actor') == 'learner' and o.get('id') not in invalid
                 and o.get('milestone') == event['milestone'] and o.get('kind') == event['kind']
                 and scopes_overlap(event, o)), 'a later observation')
            where = f"skill {skill}" if skill else f"milestone {event['milestone']}"
            require(newer is None, f"stale evidence cannot support status: {where} references "
                                   f"{eid}, but {newer} is a later overlapping {event['kind']} for "
                                   f"{event['milestone']} -- re-point this reference or reconcile it")
            if skill:
                require(skill in event['skill_ids'], 'evidence does not support this skill')
            found.append(event)
        return found

    queues = skills['review_queues']
    require(isinstance(queues, dict) and set(queues) == {'blockers', 'delayed_practice', 'role_gaps'}, 'review queue keys')
    require(all(isinstance(entries, list) and all(isinstance(q, dict) for q in entries) for entries in queues.values()), 'review entries must be objects')
    decisions = [e for e in events if e.get('kind') == 'readiness']
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
        require(m.get('status') in {'pending', 'in_progress', 'ready', 'complete'}, 'invalid milestone status')
        for kind, gate in m['gates'].items():
            require(gate.get('status') in {'pending', 'satisfied'}, 'invalid gate status')
            evidence = references(gate['evidence_ids'])
            require(all(e['kind'] == kind and e['milestone'] == mid for e in evidence), 'gate evidence kind/milestone mismatch')
            if gate['status'] == 'satisfied':
                require(evidence and all(e['outcome'] == 'pass' for e in evidence), 'satisfied gate needs current passing evidence')
                if kind in {'explanation', 'modification', 'debug', 'transfer'}:
                    require(all(e['assistance'] != 'ai_implemented' for e in evidence), 'ownership gate requires learner work')
                if mid == 'J5' and kind != 'execution':
                    require(all(e['assistance'] in {'none', 'docs'} for e in evidence), f'J5 independent ownership gate unsupported: {kind}')
                if kind == 'transfer':
                    practice = references(m['gates']['modification']['evidence_ids'])
                    require(any(p['outcome'] == 'pass' and delayed_after(t['at'], p['at'])
                                for t in evidence for p in practice), 'milestone transfer requires at least 24 hours after modification (date-only: two days)')
        if m['status'] == 'ready':
            require('transfer' in m['gates'] and m['gates']['transfer']['status'] == 'pending', 'ready requires pending retention transfer')
            require(all(g['status'] == 'satisfied' for k, g in m['gates'].items() if k != 'transfer'), 'ready milestone lacks current readiness gates')
            current_proof = {eid for k, g in m['gates'].items() if k != 'transfer' for eid in g['evidence_ids']}
            require(any(d['milestone'] == mid and set(d['evidence_ids']) == current_proof
                        and not invalid.intersection(d['evidence_ids']) for d in decisions),
                    'ready requires current durable readiness decision')
        if m['status'] == 'complete':
            require(all(g['status'] == 'satisfied' for g in m['gates'].values()), 'complete milestone has unsatisfied gates')
        if m['status'] in {'ready', 'complete'}:
            require(all(by_id[p]['status'] in {'ready', 'complete'} for p in COMPLETION_PREREQUISITES.get(mid, ())),
                    f'{mid} completion prerequisite incomplete')
    active = current.get('milestone')
    require(active in by_id, 'unknown active milestone')
    active_stage = by_id[active]['stage']
    require(current.get('stage') == active_stage and current.get('quest') == ('Q0' if active_stage == 'J0' else active_stage), 'active stage/quest mismatch')
    for mid, m in by_id.items():
        predecessors = ENTRY_PREREQUISITES.get(mid, tuple(STEPS))
        if mid == active:
            require(all(by_id[p]['status'] in {'ready', 'complete'} for p in predecessors), 'incomplete milestone prerequisite')
        if m['status'] != 'pending':
            # Reopened prerequisites do not erase work demonstrated after an earlier pass.
            own_ids = {eid for gate in m['gates'].values() for eid in gate['evidence_ids']}
            own = [e for e in learner if e['id'] in own_ids]
            for observation in own:
                started_index = events.index(observation)
                for p in predecessors:
                    prior = [e for e in events[:started_index] if e.get('actor') == 'learner']
                    historical_current = [e for e in prior if e['milestone'] == p and e['id'] not in invalid
                                          and is_fresh(e, prior)]
                    needed = set(STEPS[p])
                    if 'transfer' in needed and any(d['milestone'] == p and events.index(d) < started_index
                            and not invalid.intersection(d['evidence_ids'])
                            and all(next((e for e in historical_current if e['id'] == eid), None) is not None for eid in d['evidence_ids'])
                            and {records[eid]['kind'] for eid in d['evidence_ids']} == needed - {'transfer'}
                            for d in decisions):
                        needed.remove('transfer')
                    passing = {e['kind'] for e in historical_current if e['outcome'] == 'pass'
                               and (e['kind'] == 'execution' or e['assistance'] != 'ai_implemented')
                               and (p != 'J5' or e['kind'] == 'execution' or e['assistance'] in {'none', 'docs'})}
                    require(needed <= passing,
                            'downstream history lacks earlier prerequisite evidence')
                    if 'transfer' in needed:
                        transfers = [e for e in historical_current if e['kind'] == 'transfer' and e['outcome'] == 'pass']
                        modifications = [e for e in historical_current if e['kind'] == 'modification' and e['outcome'] == 'pass']
                        require(any(delayed_after(t['at'], pmod['at']) for t in transfers for pmod in modifications),
                                'downstream history lacks delayed prerequisite transfer')
    for row in rows:
        status = row['status']
        require(status in STATUSES, 'unknown skill status')
        evidence = references(row['evidence_ids'], row['id'])
        reconciliations = row.get('reconciliations', [])
        require(isinstance(reconciliations, list) and all(isinstance(r, dict) for r in reconciliations), 'skill reconciliations must be objects')
        for reconciliation in reconciliations:
            failure = records.get(reconciliation.get('failure_id'))
            require(failure is not None and failure.get('actor') == 'learner' and failure.get('outcome') == 'fail'
                    and row['id'] in failure['skill_ids'], 'reconciliation must name relevant failure')
            require(reconciliation.get('decision') == 'retain' and all(nonempty(reconciliation.get(k)) for k in ('reason', 'scope', 'source', 'at')), 'invalid reconciliation decision')
            require(timestamp(failure['at']) <= timestamp(reconciliation['at']) <= timestamp(skills['updated_at']), 'reconciliation time outside failure/snapshot interval')
            if root:
                local_ref(root, reconciliation['source'])
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
            require(any(delayed_after(t['at'], p['at'])
                        for t in independent if t['kind'] == 'transfer'
                        for p in independent if p['kind'] == 'modification'), 'independent transfer requires at least 24 hours after practice (date-only: two days)')
            failures = [e for e in learner if e['id'] not in invalid and row['id'] in e['skill_ids']
                        and e['outcome'] == 'fail' and events.index(e) > min(events.index(p) for p in independent)
                        and not any(p['kind'] == e['kind'] and events.index(p) > events.index(e) for p in independent)]
            for failure in failures:
                require(any(r['failure_id'] == failure['id'] for r in reconciliations),
                        f'{row["id"]} independent claim needs failure reconciliation: {failure["id"]}')
            if status == 'production_understanding':
                require('operational' in {e['kind'] for e in independent}, 'production status lacks operational evidence')
    if by_id['J5']['status'] in {'ready', 'complete'}:
        missing = [r['id'] for r in rows if r['id'] in initial_ids if r['status'] not in {'practiced', 'applied_independently', 'production_understanding'}]
        require(not missing, 'final capability coverage missing: ' + ', '.join(missing))
        if by_id['J5']['status'] == 'complete':
            require(all(by_id[mid]['status'] == 'complete' for mid in STEPS), 'final completion requires all initial-route retention complete')
            require(next(r for r in rows if r['id'] == 'E22')['status'] in {'applied_independently', 'production_understanding'}, 'final E22 delivery requires independent evidence')
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
                'docs/PROGRESS_PROTOCOL.md', 'docs/ASSESSMENT_CARDS.md', 'docs/PORTFOLIO.md', 'docs/PROVIDER_REFERENCE.md',
                'docs/PILOT.md', 'docs/MIGRATION.md', '_bmad-output/specs/spec-codex-learning-workspace/SPEC.md']
    for name in required:
        require((root/name).is_file(), f'missing owned file: {name}')
    files = [root/n for n in required] + list((root/'docs').glob('*.md')) + list((root/'_bmad-output/specs').rglob('*.md'))
    for path in set(files):
        body = path.read_text(encoding='utf-8')
        require(sum(line.strip().startswith('```') for line in body.splitlines()) % 2 == 0, f'unbalanced fence: {path.name}')
        for link in re.findall(r'(?<!!)\[[^\]\n]+\]\(([^)\n]+)\)', body):
            check_link(path, link)
    mirror = root/'.claude/skills/ai-engineering-tutor'
    if mirror.is_dir():
        # The mirror is a convenience for a second host, never a second source.
        source = root/'.agents/skills/ai-engineering-tutor'
        for path in sorted(p for p in source.rglob('*') if p.is_file()):
            twin = mirror/path.relative_to(source)
            require(twin.is_file(), f'tutor skill mirror missing {path.name}: run tools/sync_tutor_skill.py')
            require(twin.read_bytes() == path.read_bytes(),
                    f'tutor skill mirror drifted at {path.name}: run tools/sync_tutor_skill.py')
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
    setup = copy.deepcopy((c,s,events))
    setup_fail = event('execution','setup-fail',outcome='fail'); setup_fail['milestone']='0.1'
    append(setup, setup_fail); test('failed setup prerequisite is recordable', setup, True)
    misfiled = copy.deepcopy(setup)
    misfiled[0]['milestones'][0]['gates']['execution']={'status':'satisfied','evidence_ids':['setup-fail']}
    test('setup evidence cannot satisfy a 0.3 gate', misfiled, False)
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
    for kind,day in [('modification','2026-09-08'),('debug','2026-09-08'),('transfer','2026-09-10')]: append(independent,event(kind,kind,day=day))
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
    scoped=copy.deepcopy(practiced); other=event('execution','other','fail'); other['skill_ids']=['E01']; append(scoped,other)
    test('unrelated capability failure leaves passing gate current',scoped,True)
    bad=copy.deepcopy(scoped); bad[2][-1]['skill_ids']=['E03']; test('overlapping capability failure defeats pass',bad,False)
    milestone_wide=copy.deepcopy(practiced); other=event('execution','milestone-wide','fail'); other['skill_ids']=[]; append(milestone_wide,other)
    test('untagged failure remains milestone-wide',milestone_wide,False)
    located=copy.deepcopy((c,s,events)); item=event('location','loc'); item['observed_path']='C:/example/app'; append(located,item)
    located[0]['code_location'].update(path='c:\\example\\app',status='verified',evidence_id='loc'); test('exact normalized location',located,True)
    bad=copy.deepcopy(located); bad[2][-1]['observed_path']='C:/example/app-backup'; test('substring location rejected',bad,False)
    regression=copy.deepcopy(advance)
    downstream = event('execution', 'downstream'); downstream['milestone'] = '0.4'; append(regression, downstream)
    regression[0]['milestones'][1]['gates']['execution'] = {'status':'satisfied', 'evidence_ids':['downstream']}
    append(regression,event('execution','regression','fail'))
    regression[0]['milestone']='0.3'; regression[0]['milestones'][0]['status']='in_progress'
    regression[0]['milestones'][0]['gates']['execution']={'status':'pending','evidence_ids':['regression']}
    test('reassessment preserves downstream history',regression,True)
    delayed=copy.deepcopy((c,s,events)); target=delayed[0]['milestones'][6]
    for kind in ('modification','explanation','transfer'):
        item=event(kind,'delay-'+kind); item['milestone']='0.9'; append(delayed,item)
        target['gates'][kind]={'status':'satisfied','evidence_ids':[item['id']]}
    test('same day milestone transfer',delayed,False)
    delayed[2][-1]['at']='2026-09-10'; delayed[0]['updated_at']=delayed[1]['updated_at']='2026-09-10'; test('later milestone transfer',delayed,True)
    # Readiness and ownership regressions use only synthetic in-memory observations.
    ready = copy.deepcopy(delayed)
    ready[2].pop()
    ready[0]['last_event_id'] = ready[1]['last_event_id'] = ready[0]['last_learner_event'] = ready[2][-1]['id']
    ready[0]['milestones'][6]['gates']['transfer'] = {'status': 'pending', 'evidence_ids': []}
    ready[0]['milestones'][6]['status'] = 'ready'
    review = {'milestone': '0.9', 'evidence_ids': ['delay-modification'], 'eligible_after': '2026-09-10',
              'observation': 'Synthetic readiness practice', 'next_task': 'Unfamiliar variation', 'trigger': 'Later study session'}
    ready[1]['review_queues']['delayed_practice'] = [review]
    prior_events = []
    for milestone in ready[0]['milestones'][:6]:
        milestone['status'] = 'complete'
        for kind in STEPS[milestone['id']]:
            item = event(kind, 'prior-' + milestone['id'] + '-' + kind)
            item['milestone'] = milestone['id']; prior_events.append(item)
            milestone['gates'][kind] = {'status':'satisfied', 'evidence_ids':[item['id']]}
    ready[2][1:1] = prior_events
    decision = dict(review, id='ready-decision', at=ready[2][-1]['at'], kind='readiness', actor='maintainer', source='conversation:fixture', evidence_ids=['delay-modification', 'delay-explanation'])
    append(ready, decision)
    test('ready with single readiness event contract', ready, True)
    no_duplicate_queue = copy.deepcopy(ready); no_duplicate_queue[1]['review_queues']['delayed_practice'] = []
    test('ready needs no duplicate retention queue', no_duplicate_queue, True)
    bad = copy.deepcopy(no_duplicate_queue); next(e for e in bad[2] if e['kind']=='readiness').pop('next_task')
    test('readiness event needs next task', bad, False)
    bad = copy.deepcopy(no_duplicate_queue); next(e for e in bad[2] if e['kind']=='readiness')['eligible_after']='2026-09-08'
    test('readiness event rejects premature eligibility', bad, False)
    bad = copy.deepcopy(no_duplicate_queue)
    item=event('modification','stale-ready-proof','fail',day=bad[2][-1]['at']);item['milestone']='0.9';append(bad,item)
    test('later overlapping failure stales readiness proof', bad, False)
    bad = copy.deepcopy(delayed); bad[2][-3]['at'] = '2026-09-08T23:59:00Z'; bad[2][-2]['at'] = '2026-09-08T23:59:30Z'; bad[2][-1]['at'] = '2026-09-09T00:01:00Z'
    test('midnight is not delayed retention', bad, False)
    bad[2][-1]['at'] = '2026-09-09T23:59:00Z'
    test('full 24 hours is delayed retention', bad, True)
    bad = copy.deepcopy(regression)
    append(bad, {'id':'invalid-history', 'at':'2026-09-08', 'kind':'correction', 'actor':'maintainer', 'supersedes':'run', 'reason':'Synthetic false earlier output'})
    test('corrected prerequisite cannot support downstream history', bad, False)
    bad[0]['milestones'][1]['status'] = 'pending'
    test('correction preserves artifacts with reopened claims', bad, True)
    earlier_failure = copy.deepcopy(independent)
    item = event('debug', 'earlier-attempt', outcome='fail')
    earlier_failure[2].insert(1, item)
    test('same-date earlier failure resolved by later independent work', earlier_failure, True)
    failure = copy.deepcopy(independent)
    item = event('debug', 'cross-stage-fail', outcome='fail', day='2026-09-11'); item['milestone'] = 'J1'; append(failure, item)
    test('cross-stage failure cannot silently retain independence', failure, False)
    downgrade = copy.deepcopy(failure); downgrade[1]['skills'][2]['status'] = 'practiced'
    test('cross-stage failure with conservative downgrade', downgrade, True)
    failure[1]['skills'][2]['reconciliations'] = [{'failure_id':'cross-stage-fail', 'decision':'retain', 'reason':'Failure concerns unpracticed extension', 'scope':'Earlier provider boundary only', 'source':'conversation:fixture', 'at':'2026-09-11'}]
    test('cross-stage failure with scoped retain decision', failure, True)
    for field, value in [('decision','ignore'), ('scope',''), ('at','2026-09-08'), ('source','missing-source.txt')]:
        bad = copy.deepcopy(failure); bad[1]['skills'][2]['reconciliations'][0][field] = value
        test('invalid reconciliation ' + field, bad, False)
    reassessed = copy.deepcopy(failure); reassessed[1]['skills'][2].pop('reconciliations')
    item = event('debug', 'later-independent-debug', day='2026-09-12'); item['milestone'] = 'J1'; append(reassessed, item)
    reassessed[1]['skills'][2]['evidence_ids'].append(item['id'])
    test('later independent same-kind reassessment resolves failure', reassessed, True)
    route = copy.deepcopy((c,s,events))
    day = datetime(2026, 9, 8, tzinfo=timezone.utc)
    final_refs = []
    for milestone in route[0]['milestones']:
        for kind in STEPS[milestone['id']]:
            day += timedelta(days=2)
            item = event(kind, 'route-' + milestone['id'] + '-' + kind, day=day.isoformat())
            item['milestone'] = milestone['id']
            item['skill_ids'] = [f'E{i:02}' for i in range(1, 23)]
            append(route, item)
            milestone['gates'][kind] = {'status':'satisfied', 'evidence_ids':[item['id']]}
            if milestone['id'] == 'J5': final_refs.append(item['id'])
        milestone['status'] = 'complete'
    route[0].update(stage='J5', quest='J5', milestone='J5')
    for row in route[1]['skills']:
        row.update(status='practiced', evidence_ids=[final_refs[0]])
    route[1]['skills'][-1].update(status='applied_independently', evidence_ids=final_refs[1:])
    test('final independent ownership and capability coverage', route, True)
    sql_branch = copy.deepcopy(route)
    for event_row in list(sql_branch[2]):
        if event_row.get('milestone') == 'J3': sql_branch[2].remove(event_row)
    j3 = next(m for m in sql_branch[0]['milestones'] if m['id']=='J3')
    j3['status']='pending'
    for kind in STEPS['J3']: j3['gates'][kind]={'status':'pending','evidence_ids':[]}
    next(m for m in sql_branch[0]['milestones'] if m['id']=='J4')['status']='in_progress'
    next(m for m in sql_branch[0]['milestones'] if m['id']=='J5')['status']='pending'
    sql_branch[0].update(stage='J4',quest='J4',milestone='J4')
    test('J2 permits J4 SQL and scoped tool branch before J3',sql_branch,True)
    bad=copy.deepcopy(sql_branch);next(m for m in bad[0]['milestones'] if m['id']=='J4')['status']='complete'
    test('J4 combined completion still requires J3',bad,False)
    bad = copy.deepcopy(route)
    for row in bad[1]['skills']: row.update(status='not_started', evidence_ids=[])
    test('route gates alone cannot establish capability coverage', bad, False)
    bad = copy.deepcopy(route); bad[2][-1]['assistance'] = 'worked_example'
    test('worked example cannot satisfy final ownership', bad, False)
    bad = copy.deepcopy(route); bad[2][-5]['assistance'] = 'ai_implemented'
    test('assisted execution with independent ownership remains valid', bad, True)
    deferred = copy.deepcopy(route)
    j2 = next(m for m in deferred[0]['milestones'] if m['id'] == 'J2')
    j2['status'] = 'ready'; j2['gates']['transfer'] = {'status':'pending', 'evidence_ids':[]}
    practice_id = j2['gates']['modification']['evidence_ids'][0]
    practice_at = next(e['at'] for e in deferred[2] if e['id'] == practice_id)
    deferred[1]['review_queues']['delayed_practice'] = [dict(review, milestone='J2', evidence_ids=[practice_id], eligible_after=(timestamp(practice_at)+timedelta(days=2)).isoformat())]
    for m in deferred[0]['milestones']:
        if m['id'] in {'J4', 'J5'}: m['status'] = 'pending'
    deferred[0].update(stage='J3', quest='J3', milestone='J3')
    d = dict(deferred[1]['review_queues']['delayed_practice'][0], id='j2-ready', at=next(e['at'] for e in deferred[2] if e['id']=='route-J2-explanation'), kind='readiness', actor='maintainer', source='conversation:fixture', evidence_ids=['route-J2-modification','route-J2-explanation'])
    deferred[2].insert(next(i for i,e in enumerate(deferred[2]) if e['id']=='route-J2-transfer'), d)
    next(m for m in deferred[0]['milestones'] if m['id']=='J3')['status']='in_progress'
    deferred[2][:] = [e for e in deferred[2] if e['id'] != 'route-J2-transfer']
    test('pending retention permits next useful stage', deferred, True)
    final_pending = copy.deepcopy(deferred)
    for m in final_pending[0]['milestones']:
        if m['id'] in {'J3','J4','J5'}: m['status']='complete'
    final_pending[0].update(stage='J5',quest='J5',milestone='J5')
    test('final completion rejects outstanding earlier retention', final_pending, False)
    moved = copy.deepcopy(route); moved[1]['later_modules'].append(moved[1]['skills'].pop(0))
    test('E row cannot move outside coverage partition', moved, False)
    # Separate skill proof makes the gate assistance failures independent of E22 promotion.
    ownership = copy.deepcopy(route)
    skill_refs = []
    for kind in ('explanation','modification','debug','transfer'):
        day += timedelta(days=2)
        item = event(kind, 'separate-E22-' + kind, day=day.isoformat()); item['skill_ids']=['E22']
        append(ownership, item); skill_refs.append(item['id'])
    ownership[1]['skills'][-1]['evidence_ids'] = skill_refs
    # The added 0.3 explanation supersedes its gate, so keep it current.
    ownership[0]['milestones'][0]['gates']['explanation']['evidence_ids'] = [skill_refs[0]]
    test('separate independent final skill evidence', ownership, True)
    for kind in ('explanation','modification','debug','transfer'):
        bad = copy.deepcopy(ownership)
        next(e for e in bad[2] if e['id']=='route-J5-'+kind)['assistance']='worked_example'
        test('isolated J5 ownership '+kind, bad, False)
    bad = copy.deepcopy(route); bad[1]['skills'][-1].update(status='practiced', evidence_ids=[final_refs[0]])
    test('isolated final E22 independence', bad, False)
    # Genuine reassessment retains a readiness decision even after its live queue is retired.
    regressed = copy.deepcopy(deferred)
    j2 = next(m for m in regressed[0]['milestones'] if m['id']=='J2')
    item = event('modification','j2-regression','fail',day=regressed[2][-1]['at']); item['milestone']='J2'; item['skill_ids']=[]
    append(regressed,item); j2['status']='in_progress'; j2['gates']['modification']={'status':'pending','evidence_ids':[item['id']]}
    regressed[0].update(stage='J2',quest='J2',milestone='J2'); regressed[1]['review_queues']['delayed_practice']=[]
    test('durable readiness preserves downstream after practice failure',regressed,True)
    late_debug = copy.deepcopy(regressed)
    item = event('debug', 'j3-after-prerequisite-failure', day=late_debug[2][-1]['at'])
    item['milestone'] = 'J3'; item['skill_ids'] = []; append(late_debug, item)
    next(m for m in late_debug[0]['milestones'] if m['id'] == 'J3')['gates']['debug'] = {'status':'satisfied', 'evidence_ids':[item['id']]}
    test('old downstream gates cannot mask new work after prerequisite failure', late_debug, False)

    retro = copy.deepcopy(regressed); d = next(e for e in retro[2] if e['kind']=='readiness'); retro[2].remove(d)
    # Move decision after downstream began but before later regression, retaining valid then-current proof.
    index = next(i for i,e in enumerate(retro[2]) if e['id']=='route-J3-debug')+1
    d['at']=retro[2][index-1]['at']; retro[2].insert(index,d)
    test('retroactive readiness cannot authorize earlier downstream proof',retro,False)
    invalid_history = copy.deepcopy(regressed)
    append(invalid_history,dict(id='correct-j2',at=invalid_history[2][-1]['at'],kind='correction',actor='maintainer',supersedes='route-J2-modification',reason='Wrong practice artifact'))
    test('invalidated durable readiness proof cannot support downstream',invalid_history,False)
    recovered = copy.deepcopy(invalid_history)
    item=event('modification','replacement-j2',day=recovered[2][-1]['at']); item['milestone']='J2'; item['skill_ids']=[]; append(recovered,item)
    j2=next(m for m in recovered[0]['milestones'] if m['id']=='J2'); j2['gates']['modification']={'status':'satisfied','evidence_ids':[item['id']]}; j2['status']='ready'
    q=dict(review,milestone='J2',evidence_ids=[item['id']],eligible_after=(timestamp(item['at'])+timedelta(days=2)).isoformat())
    recovered[1]['review_queues']['delayed_practice']=[q]
    append(recovered,dict(q,id='replacement-ready',at=item['at'],kind='readiness',actor='maintainer',source='conversation:fixture',evidence_ids=[item['id'],'route-J2-explanation']))
    test('recovered current prerequisite cannot backfill earlier downstream proof',recovered,False)
    j3=next(m for m in recovered[0]['milestones'] if m['id']=='J3')
    for kind in STEPS['J3']:
        item=event(kind,'fresh-j3-'+kind,day=recovered[2][-1]['at']);item['milestone']='J3';item['skill_ids']=[];append(recovered,item)
        j3['gates'][kind]={'status':'satisfied','evidence_ids':[item['id']]}
    recovered[0].update(stage='J3',quest='J3',milestone='J3')
    test('fresh downstream reassessment after valid prerequisite recovers',recovered,True)
    resolved_history=copy.deepcopy(reassessed)
    resolved_history[1]['skills'][2]['reconciliations']=copy.deepcopy(failure[1]['skills'][2]['reconciliations'])
    test('resolved reconciliation remains auditable',resolved_history,True)
    for value in (None, 'bad', 12, []):
        bad=copy.deepcopy(failure);bad[1]['skills'][2]['reconciliations']=[value]
        test('malformed reconciliation '+str(value),bad,False)
    bad=copy.deepcopy(failure);bad[1]['skills'][2]['reconciliations'][0]['at']='2099-01-01'
    test('future reconciliation rejected',bad,False)
    for value in ('20260908', '2026-W37-2', '2026-09-08T23:00'):
        bad=copy.deepcopy(complete);bad[2][-1]['at']=value
        test('noncanonical evidence time '+value,bad,False)
    for keys, accepted in [(['python','uv','groq','python-dotenv'],True),
                           (['python','uv','groq'],False),
                           (['python','uv','groq','python-dotenv','langchain'],False)]:
        candidate=copy.deepcopy(complete)
        candidate[0]['provider']['installed_versions']={key:None for key in keys}
        test('provider version keys '+','.join(keys),candidate,accepted)
    for eligible, accepted in [('2026-09-09',False),('2026-09-10',True),('20260910',False)]:
        bad=copy.deepcopy(ready);next(e for e in bad[2] if e['kind']=='readiness')['eligible_after']=eligible
        test('readiness date boundary '+eligible,bad,accepted)
    require(not delayed_after('2026-09-09','2026-09-08T23:59:00Z'), 'one-day mixed delay accepted')
    require(delayed_after('2026-09-10','2026-09-08T23:59:00Z'), 'two-day mixed delay rejected')
    require(delayed_after('2026-09-10T00:01:00Z','2026-09-08'), 'reverse mixed delay rejected')
    require(not delayed_after('2026-09-10','2026-09-08T23:00:00-12:00'), 'offset mixed delay accepted')
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
    curriculum = (root/'docs/CURRICULUM.md').read_text(encoding='utf-8')
    cards = (root/'docs/ASSESSMENT_CARDS.md').read_text(encoding='utf-8')
    document_test('conditional framework no-adoption contract',
                  lambda: require('justified no-adoption' in curriculum.lower()
                                  and 'abstraction decision' in cards.lower(),
                                  'conditional framework assessment missing'), True)
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
