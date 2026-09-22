#!/usr/bin/env python3
"""
measure.py - Evaluates an Idea Scout Report against the production 7-point quality rubric.
Inspired by Caveman's evals/measure.py.
"""

import argparse
import re
import sys
from pathlib import Path

def evaluate_report(file_path: Path) -> dict:
    if not file_path.exists():
        return {"error": f"File not found: {file_path}"}

    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    scores = {}
    details = {}

    # 1. Executive Verdict (15 pts)
    # Check for Executive Summary callout and Level X indicator
    has_exec = "> **Executive Summary**" in content or "## Verdict" in content
    level_match = re.search(r"Level\s+([0-5](\.[0-9])?)\b", content, re.IGNORECASE)
    if has_exec and level_match:
        scores["verdict"] = 15
        details["verdict"] = f"Found: Level {level_match.group(1)} with executive summary"
    elif has_exec or level_match:
        scores["verdict"] = 8
        details["verdict"] = "Partial: Missing explicit Level or executive callout"
    else:
        scores["verdict"] = 0
        details["verdict"] = "Missing executive summary and maturity level"

    # 2. Concept Decomposition (10 pts)
    has_decomp = "## 🧭 Concept" in content or "Decomposition" in content or "Core Premise" in content
    has_mechanisms = "Underlying Mechanisms" in content or "Taxonomy" in content
    if has_decomp and has_mechanisms:
        scores["decomposition"] = 10
        details["decomposition"] = "Comprehensive mechanism and taxonomy breakdown"
    elif has_decomp:
        scores["decomposition"] = 5
        details["decomposition"] = "Partial: Missing explicit mechanism or taxonomy breakdown"
    else:
        scores["decomposition"] = 0
        details["decomposition"] = "Missing concept decomposition"

    # 3. 5D Radar Scorecard Table (15 pts)
    has_scorecard = "## 📊 Landscape Scorecard" in content or "Scorecard" in content
    dimensions = ["Academic", "Code", "Commercial", "Community", "Feasibility"]
    found_dims = [d for d in dimensions if d.lower() in content.lower()]
    if has_scorecard and len(found_dims) >= 4:
        scores["scorecard"] = 15
        details["scorecard"] = f"Complete scorecard table ({len(found_dims)}/5 dimensions)"
    elif has_scorecard:
        scores["scorecard"] = 8
        details["scorecard"] = f"Partial scorecard table ({len(found_dims)}/5 dimensions)"
    else:
        scores["scorecard"] = 0
        details["scorecard"] = "Missing 5D landscape scorecard"

    # 4. Citation Grounding & Links (20 pts)
    links = re.findall(r'\[([^\]]+)\]\((https?://[^\)]+)\)', content)
    github_links = [url for _, url in links if "github.com" in url]
    arxiv_links = [url for _, url in links if "arxiv.org" in url]
    star_mentions = re.findall(r'★[0-9]+(\.[0-9]+)?[km]?', content)

    link_score = 0
    if len(links) >= 3:
        link_score += 10
    elif len(links) >= 1:
        link_score += 5

    if github_links or arxiv_links:
        link_score += 5
    if star_mentions:
        link_score += 5

    scores["citations"] = link_score
    details["citations"] = f"{len(links)} external links ({len(github_links)} GitHub, {len(arxiv_links)} arXiv, {len(star_mentions)} star metrics)"

    # 5. Prior Art Matrix (15 pts)
    has_matrix = "Prior Art & Competitive Matrix" in content or "Competitive Matrix" in content
    has_table_pipes = len(re.findall(r'\|.*\|.*\|.*\|', content)) >= 3
    if has_matrix and has_table_pipes:
        scores["prior_art_matrix"] = 15
        details["prior_art_matrix"] = "Complete comparative matrix with multi-column contrast"
    elif has_matrix:
        scores["prior_art_matrix"] = 7
        details["prior_art_matrix"] = "Partial: Matrix header found but lacked structured comparison table"
    else:
        scores["prior_art_matrix"] = 0
        details["prior_art_matrix"] = "Missing Prior Art & Competitive Matrix"

    # 6. Graveyard & "Why Now?" (15 pts)
    has_graveyard = "Graveyard" in content or "Past Failure" in content or "Landmine" in content
    has_why_now = "Why Now?" in content or "Inflection" in content or "Viable Pivot" in content
    if has_graveyard and has_why_now:
        scores["graveyard_analysis"] = 15
        details["graveyard_analysis"] = "Thorough graveyard bottleneck analysis + 'Why Now?' catalyst"
    elif has_graveyard or has_why_now:
        scores["graveyard_analysis"] = 8
        details["graveyard_analysis"] = "Partial: Covered past failures or Why-Now, but not both"
    else:
        scores["graveyard_analysis"] = 0
        details["graveyard_analysis"] = "Missing Graveyard and 'Why Now?' analysis"

    # 7. Tactical Next Steps (10 pts)
    has_next_steps = "Tactical Next Steps" in content or "Next Steps" in content
    has_must_read = "Must-Read" in content or "Paper" in content
    has_wedge = "Wedge" in content or "Minimal" in content or "Prototype" in content
    if has_next_steps and (has_must_read or has_wedge):
        scores["tactical_steps"] = 10
        details["tactical_steps"] = "Actionable triad: reading foundation, inspect repo, and minimal wedge"
    elif has_next_steps:
        scores["tactical_steps"] = 5
        details["tactical_steps"] = "Partial: Next steps present but missing specific wedge"
    else:
        scores["tactical_steps"] = 0
        details["tactical_steps"] = "Missing tactical next steps"

    total = sum(scores.values())
    return {
        "file": str(file_path.name),
        "total": total,
        "passed": total >= 85,
        "scores": scores,
        "details": details
    }

def print_result(res: dict):
    print("=" * 70)
    status = "\033[92mPASS\033[0m" if res["passed"] else "\033[91mFAIL\033[0m"
    print(f"Report: {res['file']}  |  Score: {res['total']}/100  |  Status: {status}")
    print("-" * 70)
    for cat, score in res["scores"].items():
        desc = res["details"][cat]
        print(f"  • {cat.replace('_', ' ').title():<22}: {score:>2} pts  — {desc}")
    print("=" * 70 + "\n")

def main():
    parser = argparse.ArgumentParser(description="Evaluate Idea Scout Report quality")
    parser.add_argument("report", nargs="?", help="Path to report markdown file")
    parser.add_argument("--all", action="store_true", help="Evaluate all reference examples")
    args = parser.parse_args()

    root = Path(__file__).resolve().parent.parent

    if args.all:
        ex_dir = root / "examples"
        reports = list(ex_dir.glob("*.md"))
        if not reports:
            print("No examples found in examples/ directory")
            sys.exit(1)
        all_passed = True
        for r in reports:
            res = evaluate_report(r)
            print_result(res)
            if not res.get("passed", False):
                all_passed = False
        sys.exit(0 if all_passed else 1)

    if not args.report:
        print("Error: Specify a report file or use --all. Example: python3 evals/measure.py examples/sample-report-active-research.md")
        sys.exit(1)

    res = evaluate_report(Path(args.report))
    print_result(res)
    sys.exit(0 if res.get("passed", False) else 1)

if __name__ == "__main__":
    main()
