<div align="center">

# 🔭 Idea Scout

**Systematically map the prior art, academic depth, open-source code, and commercial landscape of any idea, hypothesis, or concept.**

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg?style=flat-square)](https://opensource.org/licenses/MIT)
[![Works with 30+ Agents](https://img.shields.io/badge/works_with-30%2B_agents-orange?style=flat-square)](#-supported-agents)
[![Universal Skills](https://img.shields.io/badge/skills.sh-compatible-blue?style=flat-square)](https://skills.sh)

*Stop building what already exists. Find the frontier before writing code.*

</div>

---

## ⚡ 1-Command Universal Install

Install into **every AI coding agent on your machine** (Antigravity, Claude Code, Hermes, OpenClaw, Codex, Cursor, Windsurf, Cline, Aider) in one command:

### macOS / Linux / WSL / Git Bash
```bash
curl -fsSL https://raw.githubusercontent.com/Its-Atharva-Gupta/idea-scout/main/install.sh | bash
```

### Windows (PowerShell 5.1+)
```powershell
irm https://raw.githubusercontent.com/Its-Atharva-Gupta/idea-scout/main/install.ps1 | iex
```

### Universal Agent Skills Protocol (`npx skills`)
```bash
npx skills add Its-Atharva-Gupta/idea-scout -g
# Note: For Antigravity, add the agent flag explicitly:
npx skills add Its-Atharva-Gupta/idea-scout -a antigravity -g
```

---

## 💡 The Problem: Why This Exists

Most developers who have an idea ask an LLM: *"Has anyone built X?"*
Standard LLMs hallucinate, offer vague cheerleading (*"That's a great idea with huge potential!"*), or miss the GitHub repos, arXiv papers, and dead startups that already tackled it.

**Idea Scout turns your coding agent into an empirical prior-art intelligence engine.** It searches across 6 vectors, measures exact repo health, maps academic depth, diagnoses why prior attempts died, and pinpoints the uncontested frontier.

---

## 🥊 See It: Normal Agent vs. Idea Scout

<table>
<tr>
<th width="50%">🗣️ Normal Agent (Vague & Fluffy)</th>
<th width="50%">🔭 Idea Scout Agent (Empirical & Grounded)</th>
</tr>
<tr>
<td valign="top">

> "Yes, someone has definitely worked on this! There are a few interesting projects on GitHub that try to speed up LLMs using speculative execution. It seems like a very active field right now with a lot of exciting work from top universities."

</td>
<td valign="top">

> **Verdict: Level 3.5 (Active Research / Production)**
> Saturated core technique. Tree-based speculative decoding is actively deployed in [`vllm-project/vllm`](https://github.com/vllm-project/vllm) (★32k) and [`FasterDecoding/Medusa`](https://github.com/FasterDecoding/Medusa) (★3.8k). ICML 2024 paper [EAGLE](https://arxiv.org/abs/2401.15077) achieved 3x speedup via feature drafting.
>
> **Graveyard**: High batch sizes saturate GPU bandwidth, yielding 0x speedup.
> **White Space**: Edge deployment in `llama.cpp` with 4-bit quantized draft heads.

</td>
</tr>
</table>

---

## 🧭 The 4-Phase Intelligence Pipeline

```
[Phase 0: Deconstruct & Translate] ──► 4-Register Taxonomy (Academic, Hacker, Commercial, Legacy)
         │
         ▼
[Phase 1: Multi-Vector Deep Search] ──► 6 Vectors (GitHub, arXiv, Scholar, HN/Lobste.rs, HF, Startups)
         │
         ▼
[Phase 2: Evaluate & Score]         ──► 6-Tier Maturity Rubric + 5D Radar + Graveyard Analysis
         │
         ▼
[Phase 3: Synthesize Scout Report]  ──► Scorecard + Prior Art Matrix + White Space + Tactical Wedge
```

### 1. The 6-Tier Empirical Maturity Scale
* **Level 0 (White Space)**: 0 papers, 0 codebases, 0 products. Genuinely novel.
* **Level 1 (Speculative)**: Thought pieces, forum wishes, 0–1 tangential papers, 0 code.
* **Level 2 (Emerging PoC)**: 1–5 preprints, toy repos (<150 stars), fragmented approaches.
* **Level 3 (Active Research)**: 10–50+ preprints, top-tier conference papers, maintained repos (>500 stars).
* **Level 4 (Commercial Inflection)**: Standard frameworks (>3k stars), VC-backed startups, production adoption.
* **Level 5 (Commodity Standard)**: Cloud APIs, language standard libraries, bundled free by incumbents.

### 2. Graveyard & "Why Now?" Inflection Analysis
Uncovers why past attempts died (interconnect bandwidth, compute costs, UX friction, data scarcity) and what technological catalyst (reasoning models, WebGPU, eBPF, cheap local inference) unlocks the concept today.

### 3. The Prior Art & Competitive Matrix
Direct comparison table benchmarking the user's idea against the top 2–4 closest existing codebases across Core Technique, Strengths, Weaknesses, and Key Differentiator.

### 4. Tactical Wedge Roadmap
Delivers an actionable triad:
1. **📖 Must-Read**: Foundational paper or technical discussion with exact section guidance.
2. **🛠️ Must-Inspect**: Exact repository and module to clone.
3. **🔨 Minimal Viable Wedge**: The smallest prototype that proves the novel angle without rebuilding commodity scaffolding.

---

## 🤖 Supported Agents

| Agent | Status | Command / Usage |
| :--- | :---: | :--- |
| **Google Antigravity** | ✅ Supported | `/scout <idea>` or natural language |
| **Claude Code** | ✅ Supported | `/scout` or "has anyone worked on..." |
| **Hermes Agent** | ✅ Supported | Native skill enabled on agent start |
| **OpenClaw** | ✅ Supported | Registered in workspace skills |
| **Codex CLI** | ✅ Supported | `/scout` or `npx skills add ... -a codex` |
| **Cursor** | ✅ Supported | `/scout` in Composer / Chat |
| **Windsurf** | ✅ Supported | Prompt Cascade with "scout idea: <concept>" |
| **Cline / Roo Code** | ✅ Supported | "use skill idea-scout" |
| **Aider** | ✅ Supported | Loaded via repo conventions |
| **Any Git Project** | ✅ Supported | `.agents/skills/idea-scout/` universal standard |

---

## 🧪 Quality & Verification Suite

Idea Scout includes a deterministic validation gate and automated quality benchmark:

```bash
# Deterministic linting & link verification gate
python3 scripts/validate_skill.py

# Quality benchmark (scores reference reports on 100-pt rubric)
python3 evals/measure.py --all
```

Both included reference reports score **100 / 100 points** on our quality benchmark.

---

## 📄 License

MIT © [Atharva Gupta](https://github.com/Its-Atharva-Gupta)
