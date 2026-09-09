"""Mirror the native tutor skill into .claude/skills/ so both hosts resolve it.

    python tools/sync_tutor_skill.py

`.agents/skills/ai-engineering-tutor/` is the source of truth. The mirror exists
because Claude Code reads `.claude/skills/` while the Codex convention reads
`.agents/skills/`; both copies sit at the same relative depth, so the `../../../`
document links resolve identically from either. `validate_workspace.py` fails if
they drift, so this is a checked invariant rather than a second file to maintain.
"""
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / ".agents/skills/ai-engineering-tutor"
DST = ROOT / ".claude/skills/ai-engineering-tutor"


def main():
    if not SRC.is_dir():
        print("missing source skill:", SRC)
        return 1
    DST.mkdir(parents=True, exist_ok=True)
    copied = []
    for src in sorted(SRC.rglob("*")):
        if src.is_dir():
            continue
        dst = DST / src.relative_to(SRC)
        dst.parent.mkdir(parents=True, exist_ok=True)
        if not dst.exists() or dst.read_bytes() != src.read_bytes():
            shutil.copyfile(src, dst)
            copied.append(str(src.relative_to(SRC)))
    print("synced" if copied else "already in sync", "->", DST)
    for name in copied:
        print("  ", name)
    return 0


if __name__ == "__main__":
    sys.exit(main())
