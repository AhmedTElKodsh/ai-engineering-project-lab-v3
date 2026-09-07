"""Static pack checks only; no provider requests, learner execution or host simulation."""
from pathlib import Path
import ast
import hashlib
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
LIVE = ROOT / "NotebookLM_Live_Source_Pack"
MAINT = ROOT / "Maintainer_Only"
# Materialize the generated report before resolving links to it. If interrupted,
# do not leave an old PASS result looking like the result of this invocation.
(MAINT / "V3.2_STATIC_VALIDATION_REPORT.txt").write_text(
    "V3.2 STATIC VALIDATION: IN PROGRESS\n", encoding="utf-8")
NAMES = [
    "00_Onboarding_and_Diagnostic.md", "01_AI_Engineer_Project_Quest_Map.md",
    "02_AI_Engineering_Skill_Map.md", "03_Current_Quest_Status.md",
    "04_Engineering_Playbook.md", "05_Portfolio_Index.md",
    "06_Lesson_Generation_and_Learning_Cadence.md",
]
results = []

def check(name, predicate):
    try:
        passed = bool(predicate())
        results.append(("PASS" if passed else "FAIL", name))
    except Exception as exc:
        results.append(("FAIL", f"{name}: {type(exc).__name__}: {exc}"))

def text(number):
    return (LIVE / NAMES[number]).read_text(encoding="utf-8")

def first_call(body):
    section = body.split("## 5.3 Correct first-call file", 1)[1]
    return re.search(r"```python\n(.*?)\n```", section, re.S).group(1)

check("exactly seven expected live files and no extra live artifacts",
      lambda: sorted(p.name for p in LIVE.iterdir()) == sorted(NAMES))
check("consistent V3.2 version and revision date",
      lambda: all("**Version:** V3.2 - Medical and Retail Junior Application Path" in text(i)
                  and "**Revision date:** 2026-09-07" in text(i) for i in range(7)))

def fence_check():
    for p in ROOT.rglob("*.md"):
        opened = False
        for line in p.read_text(encoding="utf-8").splitlines():
            line = re.sub(r"^(?:> ?)+", "", line).strip()
            if line.startswith("```"):
                opened = not opened
        if opened:
            return False
    return True

check("balanced plain and blockquoted Markdown code fences", fence_check)

def links_check():
    for p in ROOT.rglob("*.md"):
        for link in re.findall(r"(?<!!)\[[^\]\n]+\]\(([^)\n]+)\)", p.read_text(encoding="utf-8")):
            if link.startswith(("https://", "http://", "#")):
                continue
            if not (p.parent / link.split("#")[0]).exists():
                raise ValueError(f"missing local link in {p.name}: {link}")
    return True

check("local Markdown links resolve", links_check)
check("live source filename references resolve",
      lambda: all(ref in NAMES for i in range(7)
                  for ref in re.findall(r"\b\d{2}_[A-Za-z_]+\.md\b", text(i))))

contract = json.loads((MAINT / "ROUTE_CONTRACT.json").read_text(encoding="utf-8"))

def graph_check():
    nodes = {x["id"]: x for x in contract["stages"]}
    assert len(nodes) == len(contract["stages"])
    visited, active = set(), set()
    def visit(n):
        if n in active:
            raise ValueError("cyclic prerequisite")
        if n in visited:
            return
        active.add(n)
        for dependency in nodes[n]["depends_on"]:
            visit(dependency)
        active.remove(n)
        visited.add(n)
    for node in nodes:
        visit(node)
    initial = contract["initial_path"]
    assert initial == [f"J{i}" for i in range(6)]
    assert {n for n in nodes if nodes[n]["required_for_initial_checkpoint"]} == set(initial)
    assert all(set(nodes[n]["depends_on"]) <= set(initial) for n in initial)
    assert all(f"### {n} " in text(1) for n in initial)
    assert all(re.search(rf"\| {n} [^|]+\|", text(1)) for n in nodes if n.startswith("Q"))
    return True

check("route dependencies resolve, are acyclic, and exclude later modules from initial gates", graph_check)
check("two products appear in route, portfolio and continuity",
      lambda: all(product in text(i) for product in contract["products"] for i in (0,1,5)))
check("pending first-call state and both completion evidence types retained",
      lambda: "**Not yet recorded in this status source**" in text(3)
      and "**0.3 — First provider-native LLM SDK call**" in text(3)
      and "Real terminal output and the learner's explanation" in text(3)
      and "execution check passed; understanding is still pending" in text(6)
      and "**Milestone 0.3 complete.**" not in text(6))
check("no awarded initial skill status in curriculum migration",
      lambda: len(re.findall(r"^\| E\d\d \|.*?\| Not started \|", text(2), re.M)) == 22)
check("host-safe response extraction spelling retained",
      lambda: "response.choices[ 0 ]" in text(3)
      and all("choices[0]" not in text(i) and "choices[-1]" not in text(i) for i in range(7)))

def parse_baseline():
    tree = ast.parse(first_call(text(3)))
    return any(isinstance(node, ast.Subscript) and isinstance(node.slice, ast.Constant)
               and node.slice.value == 0 for node in ast.walk(tree))

check("preserved complete first-call Python block parses and includes zero-index access", parse_baseline)
snapshot = json.loads((MAINT / "SOURCE_BASELINE_HASHES.json").read_text(encoding="utf-8"))
source = Path(snapshot["source_directory"])
if source.exists():
    check("all original baseline files unchanged by SHA-256",
          lambda: all((source / name).is_file() and hashlib.sha256((source / name).read_bytes()).hexdigest() == digest
                      for name, digest in snapshot["sha256"].items()))
    check("first-call executable block identical to supplied baseline",
          lambda: first_call((source / "NotebookLM_Live_Source_Pack" / NAMES[3]).read_text(encoding="utf-8")) == first_call(text(3)))
else:
    results.append(("NOT RUN", "original source unavailable; preservation and baseline code equivalence cannot be rechecked"))

check("initial vs later stack and bridge sequencing updated",
      lambda: "## Core Stack" not in text(4)
      and "Bridge A follows Quest 1" not in text(4)
      and "not J3 completion gates" in text(4)
      and "not a universal employer checklist" in text(2))
check("medical, action, evaluation and vacancy boundaries explicit",
      lambda: "not clinically validated" in text(5)
      and "simulated" in text(1)
      and "held-out" in text(1)
      and "Egypt-based applicants" in text(1)
      and "not a universal hiring minimum" in text(0))

digests = {name: hashlib.sha256((LIVE / name).read_bytes()).hexdigest() for name in NAMES}
(MAINT / "LIVE_SOURCE_MANIFEST.json").write_text(json.dumps({"version": "V3.2", "sha256": digests}, indent=2) + "\n", encoding="utf-8")
failed = sum(status == "FAIL" for status, _ in results)
report = ["V3.2 STATIC VALIDATION REPORT", "Scope: local document structure and selected consistency invariants only.", ""]
report += [f"{status}: {name}" for status, name in results]
report += ["", f"STATIC RESULT: {'FAIL' if failed else 'PASS'} ({sum(s == 'PASS' for s, _ in results)} checks passed; {failed} failed)",
           "NotebookLM V3.2 host pilot: NOT RUN", "Learner execution/understanding/retention pilot: NOT RUN",
           "Provider API/model availability and runtime: NOT RUN", "Clinical validation and hiring outcome validation: NOT RUN",
           "Static checks cannot establish teaching effectiveness or job readiness."]
(MAINT / "V3.2_STATIC_VALIDATION_REPORT.txt").write_text("\n".join(report) + "\n", encoding="utf-8")
print("\n".join(report))
sys.exit(1 if failed else 0)
