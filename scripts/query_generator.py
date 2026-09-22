#!/usr/bin/env python3
"""
Idea Scout: Query Generator & Search Matrix Builder
Generates tailored, multi-platform search queries and search URLs across:
GitHub, arXiv, Google Scholar, Hacker News, Hugging Face, and YC/Product Hunt.
"""

import argparse
import urllib.parse
import sys

def build_search_matrix(concept: str, domain: str = "general"):
    concept_clean = concept.strip().strip('"')
    encoded = urllib.parse.quote(concept_clean)
    
    # Platform queries
    github_queries = [
        f'site:github.com "{concept_clean}" "README.md"',
        f'site:github.com/topics/{concept_clean.lower().replace(" ", "-")}',
        f'"{concept_clean}" (library OR framework OR toolkit) site:github.com',
        f'"awesome" "{concept_clean}" site:github.com'
    ]
    
    arxiv_queries = [
        f'site:arxiv.org/abs "{concept_clean}"',
        f'site:arxiv.org "{concept_clean}" (2024 OR 2025 OR 2026)',
        f'"{concept_clean}" (survey OR benchmark OR empirical) site:arxiv.org'
    ]
    
    scholar_queries = [
        f'"{concept_clean}" "proceedings of"',
        f'"{concept_clean}" (NeurIPS OR ICML OR ICLR OR CVPR OR SIGCOMM OR OSDI)',
        f'"{concept_clean}" survey paper'
    ]
    
    hn_queries = [
        f'site:news.ycombinator.com "Show HN" "{concept_clean}"',
        f'site:news.ycombinator.com "{concept_clean}"',
        f'site:lobste.rs "{concept_clean}"'
    ]
    
    hf_queries = [
        f'site:huggingface.co/models "{concept_clean}"',
        f'site:huggingface.co/spaces "{concept_clean}"',
        f'site:huggingface.co/papers "{concept_clean}"'
    ]
    
    commercial_queries = [
        f'site:ycombinator.com/companies "{concept_clean}"',
        f'site:producthunt.com "{concept_clean}"',
        f'"{concept_clean}" ("alternative to" OR "open source alternative" OR "competitors")'
    ]

    return {
        "concept": concept_clean,
        "domain": domain,
        "github": github_queries,
        "arxiv": arxiv_queries,
        "scholar": scholar_queries,
        "hacker_news": hn_queries,
        "hugging_face": hf_queries,
        "commercial": commercial_queries
    }

def print_markdown(matrix):
    c = matrix["concept"]
    print(f"# 🔍 Idea Scout Search Matrix for: {c}\n")
    print(f"**Target Concept**: `{c}` | **Domain**: `{matrix['domain']}`\n")
    
    sections = [
        ("🐙 GitHub & Open Source", matrix["github"]),
        ("📄 arXiv & Preprints", matrix["arxiv"]),
        ("🎓 Google Scholar & Academic", matrix["scholar"]),
        ("💬 Hacker News & Discussions", matrix["hacker_news"]),
        ("🤗 Hugging Face & Artifacts", matrix["hugging_face"]),
        ("🏢 Commercial, YC & Startups", matrix["commercial"]),
    ]
    
    for title, queries in sections:
        print(f"### {title}")
        for q in queries:
            encoded = urllib.parse.quote(q)
            print(f"- `{q}`  \n  [Direct Search Link](https://www.google.com/search?q={encoded})")
        print()

def main():
    parser = argparse.ArgumentParser(description="Idea Scout Query Matrix Generator")
    parser.add_argument("concept", nargs="*", help="The core concept or idea to scout")
    parser.add_argument("--domain", default="general", help="Specific domain (e.g. ai, systems, saas, crypto)")
    args = parser.parse_args()

    raw_concept = " ".join(args.concept).strip() if args.concept else ""
    if not raw_concept:
        print("Error: Please provide a concept. Example: query_generator.py 'speculative decoding tree attention'", file=sys.stderr)
        sys.exit(1)

    matrix = build_search_matrix(raw_concept, args.domain)
    print_markdown(matrix)

if __name__ == "__main__":
    main()
