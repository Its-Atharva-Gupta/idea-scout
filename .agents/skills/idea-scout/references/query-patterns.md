# Idea Scout: Query Patterns & Search Syntax Reference

This reference provides domain-specific search matrices, precision dorks, and query expansion techniques to ensure comprehensive, multi-platform prior art discovery.

---

## 1. The 4-Tier Taxonomy Translation Matrix

When scouting an idea, never search using only the user's raw phrasing. Translate the core concept across four distinct linguistic registers:

| Register | Purpose | Typical Vocabulary | Example (`"AI that fixes bugs in terminal"`) |
| :--- | :--- | :--- | :--- |
| **Academic / Formal** | Preprints, journals, conference proceedings | Formal taxonomies, theoretical frameworks, Greek symbols, algorithm families | `"automated program repair"`, `"neural program synthesis"`, `"LLM agent runtime error localization"` |
| **Hacker / Open Source** | GitHub, Hacker News, Lobste.rs | Descriptive compound words, tooling slang, "toy", "awesome-", CLI tools | `"terminal copilot"`, `"bash error explainer"`, `"cli debug agent"`, `"stderr auto-fix"` |
| **Product / Commercial** | Startups, Product Hunt, SaaS | User outcomes, "alternative to", "for developers", marketing buzzwords | `"AI terminal"`, `"developer productivity tool"`, `"automated DevOps troubleshooter"`, `"Warp AI alternative"` |
| **Historical / Prior Art** | Legacy implementations, defunct tools | Pre-LLM heuristics, rule-based systems, static analysis | `"rule-based exception handler"`, `"compiler error suggestion tool"`, `"thefuck"` |

---

## 2. Platform-Specific Search Dorks

### a. GitHub & Code Repositories
Goal: Uncover working codebases, libraries, active maintainers, and developer traction.

```bash
# Direct README matches for the core mechanic
site:github.com "<concept>" "README.md"

# Topic-based exploration
site:github.com/topics/<keyword>

# Filter for libraries and frameworks with demonstrable community traction
site:github.com "<concept>" (library OR framework OR toolkit) (stars OR "star history")

# Find curated resource lists
site:github.com "awesome" "<concept>"

# Look for recent active code (filter for current/recent years)
site:github.com "<concept>" "last commit" 2025 OR 2026
```

### b. arXiv & Academic Preprints
Goal: Identify foundational papers, theoretical limits, active research groups, and benchmark baselines.

```bash
# Paper abstract pages directly
site:arxiv.org/abs "<concept>"

# Date-bounded search for emerging papers
site:arxiv.org "<concept>" (2024 OR 2025 OR 2026)

# Computer Science subfield targeting
site:arxiv.org/abs "cs.AI" OR "cs.CL" OR "cs.LG" OR "cs.DC" "<concept>"

# Finding benchmark and survey papers
site:arxiv.org ("a survey on" OR "benchmark" OR "empirical study") "<concept>"
```

### c. Google Scholar & Semantic Indices
Goal: Measure citation depth, peer-reviewed acceptance, and historical evolution.

```bash
# Peer-reviewed publication query
"<concept>" (survey OR review OR meta-analysis) "proceedings of"

# Top venue filtering (CS conferences & journals)
"<concept>" (NeurIPS OR ICML OR ICLR OR ACL OR SIGMOD OR SIGCOMM OR OSDI OR SOSP)

# Citations and seminal literature discovery
"<concept>" "cited by" filetype:pdf
```

### d. Hacker News & Lobste.rs (Hacker Underground)
Goal: Find grassroots prototypes, candid critiques, architectural post-mortems, and "Show HN" projects often created 12–24 months before academic or commercial popularity.

```bash
# Show HN launches
site:news.ycombinator.com "Show HN" "<concept>"

# In-depth technical discussions and critiques
site:news.ycombinator.com ("Ask HN" OR "discussion") "<concept>"

# Lobste.rs discussions
site:lobste.rs "<concept>"
```

### e. Hugging Face & Open Artifacts
Goal: Discover pre-trained model weights, fine-tunes, datasets, interactive Spaces, and practitioner paper summaries.

```bash
# Models and weights
site:huggingface.co/models "<concept>"

# Interactive Spaces & Web Demos
site:huggingface.co/spaces "<concept>"

# Datasets and benchmarks
site:huggingface.co/datasets "<concept>"

# Community research discussion & paper pages
site:huggingface.co/papers "<concept>"
```

### f. Commercial, Startups & Venture Landscape
Goal: Check if VC funds have backed commercial competitors, if startups exist on YC/Product Hunt, or if incumbent platforms already offer this as a feature.

```bash
# Y Combinator portfolio companies
site:ycombinator.com/companies "<concept>"

# Product Hunt launches
site:producthunt.com "<concept>"

# Startup landscape & alternatives
"<concept>" ("pricing" OR "competitors" OR "alternative to" OR "open source alternative")

# Tech press & funding announcements
"<concept>" ("seed round" OR "Series A" OR "launches" OR "TechCrunch")
```

### g. Prior Art & Patent Registrations
Goal: Detect registered intellectual property, corporate defensive publications, and formal prior art filings.

```bash
# Google Patents query
site:patents.google.com "<core concept>"

# Academic dissertation and thesis repos
"<concept>" (dissertation OR thesis) "in partial fulfillment"
```

---

## 3. Domain-Specific Query Templates

### Machine Learning & Generative AI
- **Core queries**: `"<technique>" (latent OR diffusion OR autoregressive OR transformer OR distillation)`
- **Evaluation queries**: `"<technique>" (benchmark OR "state of the art" OR perplexity OR ablation)`
- **Efficiency queries**: `"<technique>" (quantization OR vLLM OR tensorrt OR latency OR memory-efficient)`

### Systems, Infrastructure & Operating Systems
- **Core queries**: `"<concept>" (eBPF OR kernel OR WASM OR distributed OR consensus OR RDMA)`
- **Performance queries**: `"<concept>" (throughput OR p99 OR tail latency OR overhead OR lock-free)`
- **Open source queries**: `"<concept>" (rust OR c++ OR zig OR go) site:github.com`

### Developer Tooling & Languages
- **Core queries**: `"<concept>" (AST OR language-server-protocol OR linter OR compiler OR tree-sitter)`
- **Ecosystem queries**: `"<concept>" (VSCode extension OR CLI tool OR plugin)`

### Local-First & Distributed Data
- **Core queries**: `"<concept>" (CRDT OR operational transformation OR SQLite OR vector search)`
- **Sync queries**: `"<concept>" (p2p OR local-first OR offline-first OR event sourcing)`

---

## 4. De-Noising & Filtering Rules

1. **Negative Operator Elimination**: Always purge unrelated homonyms:
   - For technical decentralization: `-crypto -nft -airdrop -token` (if scouting distributed systems without Web3 noise).
   - For core algorithms: `-tutorial -medium -course -geeksforgeeks` (to strip out beginner content-farm spam).
2. **Quotation Anchoring**: Put key compound phrases in double quotes (`"speculative decoding"`, `"raft consensus"`) to prevent search engines from returning generic matches on common words.
3. **Synonym Expansion**: If a search yields zero results, immediately run a relaxed variant substituting general terms (e.g., `"speculative drafting"` -> `"draft-then-verify"` or `"assisted generation"`).
