# Idea Scout: Evaluation & Quality Benchmark Suite

This directory implements an empirical testing harness for measuring the quality, grounding, and completeness of reports produced by the `idea-scout` skill, modeled after the evaluation philosophy in `JuliusBrussee/caveman`.

---

## Evaluation Architecture

```
[Curated Idea Benchmark] ──► [Agent Execution] ──► [Report Output] ──► [evals/measure.py]
 (evals/prompts/*.json)                                                     │
                                                                   Evaluates:
                                                                   - Maturity assignment
                                                                   - Citation density & links
                                                                   - Prior art matrix
                                                                   - Graveyard & "Why Now?"
                                                                   - Actionable tactical wedge
```

---

## The 7-Point Scoring Rubric (100-Point Scale)

Every evaluated Idea Scout Report is objectively scored across 7 deterministic criteria:

| Criterion | Points | Evaluation Check |
| :--- | :---: | :--- |
| **1. Executive Verdict** | 15 | Clear 1–2 sentence summary with an explicit 0–5 maturity level. |
| **2. Taxonomy Decomposition** | 10 | Explicit core CS primitives, problem space, and multi-register keywords. |
| **3. 5D Radar Scorecard** | 15 | Complete markdown table scoring Academic, Code, Market, Community, and Feasibility. |
| **4. Citation Grounding** | 20 | Real clickable links (`https://github.com/...`, `https://arxiv.org/abs/...`), star counts, and dates. Zero ungrounded placeholders. |
| **5. Prior Art Matrix** | 15 | Comparative table contrasting ≥2 existing projects against the user's concept across technique, strengths, and weaknesses. |
| **6. Graveyard & "Why Now?"** | 15 | Identifies past failure modes / structural bottlenecks and what modern technical catalyst unlocks the idea today. |
| **7. Tactical Wedge Roadmap** | 10 | Actionable triad: Must-Read paper, Must-Inspect repo, and Minimal Viable Prototype. |

**Passing Threshold**: ≥ 85 / 100 points.

---

## Running the Quality Benchmark

To score any generated markdown report:

```bash
python3 evals/measure.py examples/sample-report-active-research.md
```

To evaluate all reference examples in batch:

```bash
python3 evals/measure.py --all
```
