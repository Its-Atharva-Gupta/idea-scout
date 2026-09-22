# Idea Scout: Report Templates & Formats

This reference contains production-ready markdown templates for formatting Idea Scout findings. Use the Flagship Template for full deep-dives, the Lightning Template for rapid checks, or the Venture/Startup Wedge Template for commercial queries.

---

## 1. Flagship Template: Full Deep-Dive Scout Report

```markdown
# 🔭 Idea Scout Report: <Crisp 3–6 Word Title>

> **Executive Summary**: <1–2 sentence direct answer: Does this exist? What is the maturity level, and where does the open frontier lie?>

---

## 🧭 Concept Formulation & Decomposition

* **Core Premise**: <1–2 sentence sharp restatement of the idea>
* **Underlying Mechanisms**: `<Primitive 1>`, `<Primitive 2>`, `<Primitive 3>`
* **Primary Target Use Case**: <Specific problem being solved for a specific audience>
* **Key Taxonomy Terms**: `<Academic Term>`, `<Hacker Slang>`, `<Commercial Keyword>`

---

## 📊 Landscape Scorecard

| Dimension | Rating (1–5) | Current State Summary |
| :--- | :--- | :--- |
| **Maturity Level** | **Level X — <Name>** | <One-sentence verdict on overall ecosystem readiness> |
| **Academic Depth** | <1 to 5> / 5 | <Preprints vs peer-reviewed; top conferences publishing> |
| **Code Ecosystem** | <1 to 5> / 5 | <Repo count, star density, maintenance health, standard libraries> |
| **Commercial Density** | <1 to 5> / 5 | <Startup activity, big tech features, VC backing> |
| **Community Mindshare** | <1 to 5> / 5 | <HN/Reddit reception, tutorials, buzz vs silence> |
| **Technical Feasibility** | <1 to 5> / 5 | <Plug-and-play today vs heavy engineering vs fundamental research> |

---

## 🔍 Multi-Platform Deep Dive

### 🐙 1. GitHub & Open Source Ecosystem
* **Landscape State**: <Active (>1k stars, recent commits) | Fragmented | Dormant / Stale | None found>
* **Notable Repositories**:
  1. [`org/repo-one`](https://github.com/...) ★<stars> — <Concise description: language, architecture, status>
  2. [`org/repo-two`](https://github.com/...) ★<stars> — <Concise description: language, architecture, status>
  3. [`org/repo-three`](https://github.com...) ★<stars> — <Concise description: language, architecture, status>
* **Health & Maintenance**: <Are repos actively maintained in 2025/2026, or did commits halt?>

### 📄 2. arXiv & Cutting-Edge Research
* **Preprint Volume**: <~N papers found | Date range: YYYY–YYYY | Velocity: Accelerating / Plateaued>
* **Landmark Papers**:
  * *"<Paper Title 1>"* (<Authors/Lab>, <Year>) — <Key contribution or theoretical breakthrough>
  * *"<Paper Title 2>"* (<Authors/Lab>, <Year>) — <Key contribution or theoretical breakthrough>
* **Leading Institutions**: <e.g., Stanford, Berkeley, MIT, Google DeepMind, Tsinghua, Meta FAIR>
* **Key Venues**: <NeurIPS, ICML, ICLR, CVPR, OSDI, SIGCOMM, etc.>

### 💬 3. Hacker News & Developer Discussions
* **Community Sentiment**: <Enthusiastic | Skeptical | Lukewarm | Unexplored>
* **Key Discussion Threads**:
  * [Show HN: <Project Title>](https://news.ycombinator.com/item?id=...) — <Community reaction summary and top critique>
  * [Discussion: <Topic>](https://news.ycombinator.com/item?id=...) — <Primary architectural bottlenecks raised by devs>
* **Developer Consensus**: <What do real engineers say is hard about this?>

### 🤗 4. Hugging Face & Applied Artifacts
* **Model Checkpoints**: <Specific weights/adapters available, or "None">
* **Datasets & Benchmarks**: <Standard evaluation datasets available, or "None">
* **Interactive Demos**: <Spaces links or interactive demos found>

### 🏢 5. Commercial Startups & Industry Incumbents
* **Venture-Backed Startups**:
  * `<Company Name>` (<Funding stage, e.g., Seed / Series A>) — <One-line product positioning>
* **Incumbent Risk**: <Is this already a built-in feature of OpenAI, Google, AWS, GitHub, Apple, etc.?>

---

## 🥊 Prior Art & Competitive Matrix

| Project / Company | Core Technique | Strengths | Critical Gaps & Weaknesses | How User's Idea Differs |
| :--- | :--- | :--- | :--- | :--- |
| **<Prior Art A>** | <Approach> | <Strength> | <Limitation / Flaw> | <Differentiating Angle> |
| **<Prior Art B>** | <Approach> | <Strength> | <Limitation / Flaw> | <Differentiating Angle> |
| **<Prior Art C>** | <Approach> | <Strength> | <Limitation / Flaw> | <Differentiating Angle> |

---

## ⚠️ Graveyard & Landmine Analysis

* **Past Failure Modes**: <Why did prior attempts fail or lose momentum? (e.g. inference latency, lack of high-quality training data, UX friction)>
* **The "Feature vs. Product" Trap**: <Could this be rendered obsolete by the next foundation model update or OS release?>
* **The "Why Now?" Inflection**: <What technical or economic breakthrough (e.g., cheap inference, WebGPU, reasoning models) makes this viable *right now* when it wasn't 2 years ago?>

---

## 🗺️ The Uncontested Frontier (White Space)

* **Unsolved Gaps**:
  1. <Specific technical gap no one has solved yet>
  2. <Specific ergonomic or developer-experience gap>
  3. <Underserved vertical or application domain>
* **The Winning Wedge**: <The specific, narrow angle where a builder has an unfair advantage>

---

## 🚀 Tactical Next Steps

1. **📖 Must-Read Paper / Post**:
   * [<Title of foundational paper/thread>](<URL>) — *Read section X to understand the baseline math/architecture.*
2. **🛠️ Must-Inspect Codebase**:
   * [`<repo/name>`](<URL>) — *Clone this repo to inspect how they implemented mechanism Y.*
3. **🔨 Minimal Viable Wedge to Build**:
   * *<Describe the single smallest, high-signal prototype that tests the novel hypothesis without wasting weeks building solved commodity infrastructure.>*
```

---

## 2. Lightning Template: Quick Scout (Under 60 Seconds)

Used when the user asks a quick query like *"Has anyone built an open-source clone of Cursor with local Ollama?"*

```markdown
# ⚡ Quick Scout: <Idea Name>

**Verdict**: **Level <X> (<Name>)** — <1-2 sentences on existence, state, and best option>

### 🏆 Top 3 Existing Implementations
1. [`<repo-name>`](<URL>) ★<stars> — <1-line summary: why it matches or differs>
2. [`<repo-name>`](<URL>) ★<stars> — <1-line summary: why it matches or differs>
3. [`<repo-name>`](<URL>) ★<stars> — <1-line summary: why it matches or differs>

### 🔍 State of the Art & Gaps
* **What's already solved**: <Solved capability>
* **What's still missing**: <Open problem>

### 💡 Bottom Line
<1-sentence advice: fork existing repo X, or build novel wedge Y.>
```
