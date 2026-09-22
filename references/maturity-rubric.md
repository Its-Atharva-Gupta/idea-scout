# Idea Scout: Maturity Rubric & Landscape Evaluation Framework

This document outlines the evaluation criteria, scoring rubric, and failure analysis methodologies used to evaluate the maturity, trajectory, and viability of an idea.

---

## 1. The 6-Tier Empirical Maturity Scale

Every researched concept is assigned an unambiguous maturity rating from Level 0 to Level 5 based on verifiable empirical evidence:

```
[Level 0: White Space] ──► [Level 1: Speculative] ──► [Level 2: Emerging PoC]
                                                            │
[Level 5: Commodity Standard] ◄── [Level 4: Production] ◄───┘ [Level 3: Active Research]
```

### Level 0: Pure Unexplored White Space
* **Definition**: No direct implementations, papers, products, or substantive technical discussions found anywhere on the public internet.
* **Empirical Signals**:
  * GitHub: 0 relevant repositories (or only unrelated name collisions).
  * arXiv / Scholar: 0 papers combining these exact mechanisms or problem formulations.
  * Commercial: 0 companies or stealth startups addressing this exact thesis.
* **Interpretation**: Genuinely novel, an unrecognized breakthrough, or syntactically described using non-standard vocabulary. Requires a secondary pass with generalized conceptual taxonomy before confirming.

### Level 1: Speculative & Conceptual Exploration
* **Definition**: Discussed conceptually as a theoretical possibility or wish-list item, but lacks functioning implementations or formal academic validation.
* **Empirical Signals**:
  * Forum posts, Reddit/HN comments, Twitter/X threads saying "Someone should build X".
  * Casual blog posts or thought-leadership pieces without benchmark results or code.
  * 0–1 tangential papers mentioning the concept in "Future Work" sections.
  * Zero runnable code or public repositories with active commits.
* **Interpretation**: High theoretical interest, low practical execution. Ample room to be first-to-code.

### Level 2: Emerging Prototype (Proof-of-Concept)
* **Definition**: Initial experimental proofs-of-concept and exploratory preprints exist. The community knows it is possible, but no consensus approach or stable architecture has crystallized.
* **Empirical Signals**:
  * 1–5 arXiv preprints (typically from university labs or independent researchers).
  * 1–3 GitHub repositories (often hackathon projects, experimental notebooks, or solo dev repos with <150 stars).
  * No standard libraries, pip packages, or plug-and-play modules.
  * Known heavy limitations (e.g., slow inference, fragile edge cases, poor generalization).
* **Interpretation**: High opportunity for engineers and researchers to introduce the first clean, performant, and ergonomic implementation.

### Level 3: Active Research & Competing Paradigms
* **Definition**: Multiple established research labs and open-source developers are actively publishing, benchmarking, and competing.
* **Empirical Signals**:
  * 10–50+ arXiv preprints across multiple top-tier venues (NeurIPS, ICML, ICLR, CVPR, OSDI, etc.).
  * Multiple maintained GitHub repositories (>500+ stars) with recent commits within 90 days.
  * Dedicated Hugging Face Spaces or model checkpoints available.
  * Tutorials, technical explainers, and YouTube walkthroughs emerging.
  * Competing architectural approaches fighting for dominance.
* **Interpretation**: Validated problem space. Differentiation requires solving key bottlenecks (latency, cost, accuracy) rather than re-proving feasibility.

### Level 4: Production-Grade / Commercial Inflection
* **Definition**: Clear winners have emerged in open source and venture-backed startups. Toolkits are stable, venture capital has flowed into the category, and early enterprise customers are in production.
* **Empirical Signals**:
  * 1–3 de facto standard frameworks or libraries (>3,000+ stars) with formal semantic versioning.
  * Survey papers published summarizing the field.
  * Multiple funded startups (Seed through Series B) or established products offering this commercially.
  * Pre-trained foundation weights, dedicated APIs, or SaaS dashboards.
* **Interpretation**: Saturated mainstream path. Entering this space requires a sharp wedge, 10x cost/speed improvement, or vertical specialization.

### Level 5: Standardized, Commercial Commodity
* **Definition**: The concept is fully commoditized, battle-tested, integrated into cloud platforms, taught in university curricula, or built into operating systems / browsers.
* **Empirical Signals**:
  * Managed cloud services (AWS, GCP, Azure, Cloudflare) provide it as a single-click API.
  * Standard library or core package ecosystem adoption (e.g., integrated into PyTorch, vLLM, Linux kernel).
  * Incumbent software giants bundle it for free as a minor feature.
* **Interpretation**: Commodity. Do not build a standalone general product here unless reinventing the fundamental cost/physics curve.

---

## 2. The 5-Dimensional Landscape Scorecard

Rate each of the five dimensions from **Low (1)** to **High (5)**:

| Dimension | Description | Low (1) | Moderate (3) | High (5) |
| :--- | :--- | :--- | :--- | :--- |
| **Academic Rigor** | Formal theory, peer review, mathematical proofs | 0 preprints | Active arXiv papers, multiple labs | Textbooks, surveys, decades of peer-reviewed literature |
| **Code Ecosystem** | Reproducibility, libraries, repo health | No code or broken snippets | Usable GitHub repos with setup instructions | Polished, pip/npm-installable libraries with CI/CD and >5k stars |
| **Commercial Density** | Startups, VC funding, incumbent features | Zero monetization | A few early-stage startups or indie hackers | Multi-billion dollar venture category; big tech features |
| **Community Mindshare** | Developer excitement, chatter, tutorials | Crickets | Regular Reddit/HN threads, Discord channels | Mainstream buzz, conference keynotes, widespread tutorials |
| **Technical Feasibility** | Solvability with today's technology | Blocked by fundamental limits / uninvented tech | Challenging engineering, fragile edge cases | Solved problem; turn-key APIs available |

---

## 3. Graveyard & Failure Analysis

When an idea appears "unexplored" or "abandoned" (e.g., popular repos untouched since 2019), it frequently suffered from a structural failure mode. Analyze which trap previous builders fell into:

1. **The Latency / Compute Trap**:
   - The idea worked conceptually in notebooks, but real-time latency or inference compute made it commercially unviable.
2. **The Data Scarcity Trap**:
   - The technique required high-quality paired training data or ground truth labels that do not exist or are prohibitively expensive to create.
3. **The UX / Friction Trap**:
   - The workflow required users to alter deeply ingrained habits, install complex dependencies, or tolerate high error rates.
4. **The Feature, Not a Product Trap**:
   - A standalone startup tried to sell a capability that incumbent platforms (OS, IDE, foundation model provider) integrated natively for free.
5. **The Fragile Edge Case Trap**:
   - The system achieved 85% accuracy easily, but the remaining 15% of failures caused catastrophic consequences (e.g. data loss, legal liability).

---

## 4. The "Why Now?" Inflection Test

If an idea failed in the past or remained dormant, determine what recent macro catalyst changes the calculus today:

* **Foundation Model Capability**: Reasoning models (e.g., o1/Gemini 2.0 Flash/Claude 3.5 Sonnet), long context (1M+ tokens), multimodal inputs.
* **Client & Edge Hardware**: WebGPU in browsers, Apple Silicon Neural Engine, local NPU acceleration, quantized SLMs (<3B parameters).
* **Network & Systems Primitives**: eBPF, WebTransport, HTTP/3, vector database innovations, fast local databases (DuckDB, SQLite WASM).
* **Economics**: 100x collapse in token pricing and cloud compute costs over the last 24 months.
* **Market & Regulatory Inflection**: New compliance requirements (EU AI Act, HIPAA updates, privacy mandates) forcing on-prem or local-first architectures.
