"""Package and verify the finished guides without touching original source files."""
from pathlib import Path
import hashlib
import json
import subprocess
import sys
import zipfile

parent = Path(__file__).resolve().parent
root = parent / "V3.2_Medical_and_Retail_Junior_Path"
subprocess.run([sys.executable, str(root / "Maintainer_Only" / "validate_v3_2.py")], check=True)

archives = [
    (parent / "V3.2_Full_Guide_Pack.zip", root, root.rglob("*")),
    (parent / "V3.2_NotebookLM_Live_Sources.zip", root / "NotebookLM_Live_Source_Pack",
     (root / "NotebookLM_Live_Source_Pack").glob("*.md")),
]
records = {}
for destination, base, candidates in archives:
    files = sorted(p for p in candidates if p.is_file() and "__pycache__" not in p.parts)
    with zipfile.ZipFile(destination, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for file in files:
            archive.write(file, file.relative_to(base).as_posix())
    with zipfile.ZipFile(destination) as archive:
        assert archive.testzip() is None
        assert sorted(archive.namelist()) == sorted(p.relative_to(base).as_posix() for p in files)
        for file in files:
            assert archive.read(file.relative_to(base).as_posix()) == file.read_bytes()
    records[destination.name] = {"files": len(files), "sha256": hashlib.sha256(destination.read_bytes()).hexdigest(), "archive_content_verified": True}
    print(f"ARCHIVE VERIFIED: {destination.name} ({len(files)} files)")
(parent / "V3.2_ARCHIVE_MANIFEST.json").write_text(json.dumps(records, indent=2) + "\n", encoding="utf-8")
