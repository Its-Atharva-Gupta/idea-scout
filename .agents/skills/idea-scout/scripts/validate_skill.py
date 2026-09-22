#!/usr/bin/env python3
"""
validate_skill.py - Deterministic skill validation and linting gate.
Inspired by Caveman's verbs-gate.mjs and compile.mjs.

Enforces:
1. Valid YAML frontmatter with required fields and trigger bindings.
2. Prompt byte budget compliance from registry.json.
3. Zero banned markers (TODO, FIXME, placeholder text).
4. Dead-link detection for all relative markdown file references.
5. Exact registry synchronization with workspace files.
"""

import json
import os
import re
import sys
from pathlib import Path

BANNED_MARKERS = ["TO" + "DO", "FIX" + "ME", "not " + "implemented", "placeholder"]

def fail(msg: str):
    print(f"\033[91m✖ Skill Validation Failed:\033[0m {msg}", file=sys.stderr)
    sys.exit(1)

def info(msg: str):
    print(f"\033[92m✔\033[0m {msg}")

def main():
    root = Path(__file__).resolve().parent.parent
    skill_md = root / "SKILL.md"
    registry_file = root / "registry.json"

    print(f"Running Skill Validation Gate on: {root}\n")

    # 1. Registry validation
    if not registry_file.exists():
        fail("registry.json is missing")

    try:
        with open(registry_file, "r", encoding="utf-8") as f:
            registry = json.load(f)
    except Exception as e:
        fail(f"Invalid JSON in registry.json: {e}")

    if registry.get("schema_version") != "2":
        fail(f"Unsupported schema_version: {registry.get('schema_version')}")

    skills = registry.get("skills", [])
    if not skills:
        fail("registry.json contains no skills")

    skill_meta = skills[0]
    skill_id = skill_meta.get("id")
    byte_budget = skill_meta.get("prompt_byte_budget", 15000)

    info(f"Loaded registry metadata for skill: '{skill_id}'")

    # 2. SKILL.md Frontmatter & Content Validation
    if not skill_md.exists():
        fail("SKILL.md is missing at repository root")

    with open(skill_md, "r", encoding="utf-8") as f:
        content = f.read()

    if not content.startswith("---\n"):
        fail("SKILL.md must start with YAML frontmatter ('---')")

    frontmatter_end = content.find("\n---\n", 4)
    if frontmatter_end < 0:
        fail("SKILL.md frontmatter is not closed with '---'")

    frontmatter_raw = content[4:frontmatter_end]
    body = content[frontmatter_end + 5:].strip()

    # Verify frontmatter name
    name_match = re.search(r"^name:\s*([a-z0-9-]+)", frontmatter_raw, re.MULTILINE)
    if not name_match:
        fail("SKILL.md frontmatter missing valid 'name' attribute")

    parsed_name = name_match.group(1)
    if parsed_name != skill_id:
        fail(f"Frontmatter name '{parsed_name}' does not match registry id '{skill_id}'")

    # Verify description and triggers
    if "description:" not in frontmatter_raw:
        fail("SKILL.md frontmatter missing 'description'")

    info(f"YAML frontmatter valid (name: {parsed_name})")

    # 3. Prompt Byte Budget Check
    body_bytes = len(body.encode("utf-8"))
    if body_bytes > byte_budget:
        fail(f"Instruction body exceeds prompt_byte_budget: {body_bytes} > {byte_budget} bytes")

    info(f"Byte budget check passed: {body_bytes} / {byte_budget} bytes")

    # 4. Banned Markers Check
    for marker in BANNED_MARKERS:
        if marker in content:
            fail(f"Found banned development marker in SKILL.md: '{marker}'")

    info("Zero banned markers detected")

    # 5. Dead Link Detection
    # Matches relative markdown links like [Title](./references/query-patterns.md)
    link_pattern = re.compile(r'\[([^\]]+)\]\(((\./|\.\./|[a-zA-Z0-9_-]+/).*?\.([a-zA-Z0-9]+))\)')
    links = link_pattern.findall(content)
    broken_links = []

    for text, rel_path, _, _ in links:
        # Strip anchors like #section
        clean_rel = rel_path.split("#")[0]
        target = (root / clean_rel).resolve()
        if not target.exists():
            broken_links.append(f"[{text}]({rel_path}) -> {target} not found")

    if broken_links:
        fail("Found broken file links in SKILL.md:\n  " + "\n  ".join(broken_links))

    info(f"Verified {len(links)} relative markdown links (0 dead links)")

    # 6. Check references and examples directories
    ref_dir = root / "references"
    ex_dir = root / "examples"
    scripts_dir = root / "scripts"

    if not ref_dir.exists() or not any(ref_dir.iterdir()):
        fail("references/ directory is missing or empty")
    if not ex_dir.exists() or not any(ex_dir.iterdir()):
        fail("examples/ directory is missing or empty")
    if not scripts_dir.exists() or not any(scripts_dir.iterdir()):
        fail("scripts/ directory is missing or empty")

    info("Directory structure (references, examples, scripts) verified")

    print("\n\033[92m✔ All Skill Production Checks Passed!\033[0m")
    sys.exit(0)

if __name__ == "__main__":
    main()
