# 🔭 Install Idea Scout

One command installs Idea Scout into every AI coding agent on your machine.

---

## ⚡ 1-Command Universal Install

### macOS / Linux / WSL / Git Bash
```bash
curl -fsSL https://raw.githubusercontent.com/Its-Atharva-Gupta/idea-scout/main/install.sh | bash
```

### Windows (PowerShell 5.1+)
```powershell
irm https://raw.githubusercontent.com/Its-Atharva-Gupta/idea-scout/main/install.ps1 | iex
```

### Universal Agent Skills Standard (`npx skills`)
```bash
npx skills add Its-Atharva-Gupta/idea-scout -g
```

---

## What the 1-Liner Does

1. **Auto-Detects Installed Agents**: Probes your environment for Google Antigravity, Claude Code, Hermes Agent, OpenClaw, Codex CLI, Cursor, Windsurf, Cline/Roo, and Aider.
2. **Copies Full Progressive Disclosure Skill Package**:
   * `SKILL.md` (Core directive, persistence, drop/keep rules, contrastive examples, safety circuit breakers)
   * `registry.json` (Schema v2 manifest)
   * `references/` (Search patterns, maturity rubric, report templates)
   * `examples/` (100/100 benchmark reference reports)
   * `scripts/` (Automated query generator and validation gate)
3. **Zero Configuration**: Binds `/scout`, `/idea-scout`, and natural language triggers immediately.

---

## Per-Agent Reference Matrix

| Agent | Native Install Location | How to Invoke |
| :--- | :--- | :--- |
| **Google Antigravity** | `~/.gemini/antigravity/skills/idea-scout` & `~/.gemini/config/skills/idea-scout` | `/scout <idea>` or "scout this concept" |
| **Claude Code** | `~/.claude/skills/idea-scout` | `/scout` or "has anyone built..." |
| **Hermes Agent** | `~/.hermes/skills/idea-scout` (or `$HERMES_HOME`) | Native skill active on agent start |
| **OpenClaw** | `~/.openclaw/workspace/skills/idea-scout` | Available in workspace skills registry |
| **Codex CLI** | `~/.codex/skills/idea-scout` | `/scout` or `npx skills add ... -a codex` |
| **Cursor** | `~/.cursor/skills/idea-scout` | `/scout` in Composer / Chat |
| **Windsurf** | `~/.codeium/windsurf/skills/idea-scout` | Prompt Cascade with "scout idea: <concept>" |
| **Cline / Roo Code** | `~/.cline/skills/idea-scout` / `~/.roo/skills/idea-scout` | "use skill idea-scout" |
| **Aider** | `~/.aider/skills/idea-scout` | Loaded via repo conventions |
| **Any Project / Repo** | `.agents/skills/idea-scout/` | Automatic repository-level discovery |

---

## CLI Flags & Options

```bash
# Preview what would be installed without writing any files
bash install.sh --dry-run

# Install into ALL supported agent environments regardless of detection
bash install.sh --all

# Install into a single target agent
bash install.sh --only hermes
bash install.sh --only openclaw
bash install.sh --only claude
bash install.sh --only antigravity

# Install into current project/workspace (.agents/skills)
bash install.sh --workspace

# List all supported agents and detection status
bash install.sh --list

# Cleanly uninstall idea-scout from all agents
bash install.sh --uninstall
```
