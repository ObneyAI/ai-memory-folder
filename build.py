#!/usr/bin/env python3
"""Build the three starter archives and check their structure. Author: Codex."""
from pathlib import Path
from urllib.parse import unquote, urlsplit
import hashlib
import json
import re
import tempfile
import zipfile

ROOT = Path(__file__).resolve().parent
SEEDS = {"AGENTS.md", "Start Here.md", "_setup.md", "About This Folder.md"}
VERSIONS = {"claude": SEEDS | {"CLAUDE.md"}, "chatgpt": SEEDS, "grokbot": SEEDS}


def prose_sentences(text):
    """Return prose fragments for a conservative length check, not a grammar check."""
    text = re.sub(r"\A---\n.*?\n---\n", "", text, flags=re.S)
    text = re.sub(r"```.*?```", "", text, flags=re.S)
    text = re.sub(r"`[^`]+`", "CODE", text)
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    text = re.sub(r"https?://\S+", "URL", text)
    for number, line in enumerate(text.splitlines(), 1):
        line = re.sub(r"^\s*(?:[-*>]\s*|\d+\.\s*|\[[ x]\]\s*)+", "", line)
        if not line or line.startswith(("#", "|")):
            continue
        for sentence in re.split(r"(?<=[.!?])\s+", line):
            words = re.findall(r"[\w]+(?:[’'-][\w]+)*", sentence)
            yield number, sentence, len(words)


def main():
    manifest = {"schema_version": 1, "kit_id": "obney-ai-memory", "kit_version": "0.4.0", "versions": {}}
    for version, names in VERSIONS.items():
        folder = ROOT / version / "AI Memory"
        actual = {p.name for p in folder.iterdir()}
        assert actual == names, (version, "Unexpected starting files", actual ^ names)
        assert all(p.is_file() and not p.is_symlink() for p in folder.iterdir())
        assert not any((ROOT / version).rglob(".git")), "Nested Git repository"
        instructions = (folder / "AGENTS.md").read_text()
        for key, value in {"kit_id": manifest["kit_id"], "kit_variant": version,
                           "kit_version": manifest["kit_version"]}.items():
            assert f"{key}: {value}\n" in instructions, (version, "Missing kit identity", key)
        entries = []
        for name in sorted(names):
            path = folder / name
            data = path.read_bytes()
            entries.append({"name": name, "source": path.relative_to(ROOT).as_posix(),
                            "sha256": hashlib.sha256(data).hexdigest(), "bytes": len(data)})
        manifest["versions"][version] = {"directory": f"{version}/AI Memory", "files": entries}
        archive = ROOT / version / "ai-memory.zip"
        with zipfile.ZipFile(archive, "w", zipfile.ZIP_DEFLATED) as output:
            for entry in entries:
                # Fixed metadata keeps repeated builds byte-for-byte stable.
                info = zipfile.ZipInfo("AI Memory/" + entry["name"], (2026, 10, 14, 0, 0, 0))
                info.compress_type = zipfile.ZIP_DEFLATED
                info.external_attr = 0o644 << 16
                output.writestr(info, (folder / entry["name"]).read_bytes())
        with tempfile.TemporaryDirectory(prefix="ai-memory-check-") as temp:
            with zipfile.ZipFile(archive) as output:
                assert output.testzip() is None
                assert set(output.namelist()) == {"AI Memory/" + n for n in names}
                output.extractall(temp)
            for entry in entries:
                assert (Path(temp) / "AI Memory" / entry["name"]).read_bytes() == (folder / entry["name"]).read_bytes()
    (ROOT / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")
    common = [(ROOT / version / "AI Memory" / "AGENTS.md").read_text().split(
        "# AI Memory instructions\n", 1)[1].split("## Saved workflows", 1)[0] for version in VERSIONS]
    assert common.count(common[0]) == len(common), "Common agent instructions differ"
    setup = [(ROOT / version / "AI Memory" / "_setup.md").read_bytes() for version in VERSIONS]
    assert setup.count(setup[0]) == len(setup), "Setup checklists differ"
    errors = []
    links = 0
    sentences = 0
    for path in sorted(ROOT.rglob("*.md")):
        if ".git" in path.relative_to(ROOT).parts:
            continue
        text = path.read_text()
        for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", text):
            if urlsplit(target).scheme or target.startswith("#"):
                continue
            links += 1
            destination = (path.parent / unquote(target.split("#")[0])).resolve()
            if not destination.is_file():
                errors.append(f"Broken link: {path.relative_to(ROOT)} -> {target}")
        if "—" in text:
            errors.append(f"Em dash: {path.relative_to(ROOT)}")
        if re.search(r"\b(?:don't|can't|isn't|won't|doesn't|you've|we're)\b", text, re.I):
            errors.append(f"Contraction: {path.relative_to(ROOT)}")
        for line, sentence, count in prose_sentences(text):
            sentences += 1
            # Apply the stricter procedural limit throughout participant and agent prose.
            if count > 20:
                errors.append(f"{path.relative_to(ROOT)}:{line}: {count} words: {sentence}")
    if errors:
        raise SystemExit("\n".join(errors))
    print(json.dumps({"files": {key: len(value) for key, value in VERSIONS.items()},
                      "starting_subfolders": 0, "relative_links": links,
                      "prose_fragments_checked": sentences, "archives_verified": 3}, indent=2))


if __name__ == "__main__":
    main()
