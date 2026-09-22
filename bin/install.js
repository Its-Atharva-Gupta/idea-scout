#!/usr/bin/env node
/**
 * Idea Scout — Unified Cross-Platform Installer
 * Installs idea-scout into any supported AI coding agent:
 * Antigravity, Claude Code, Hermes, OpenClaw, Codex, Cursor, Windsurf, Cline/Roo, Aider.
 * Pure Node.js standard library — zero npm runtime dependencies.
 */

'use strict';

const fs = require('fs');
const os = require('os');
const path = require('path');
const { execSync } = require('child_process');

const REPO = 'Its-Atharva-Gupta/idea-scout';
const HOME = os.homedir();
const CWD = process.cwd();

const COLORS = {
  reset: '\x1b[0m',
  bold: '\x1b[1m',
  green: '\x1b[32m',
  yellow: '\x1b[33m',
  blue: '\x1b[34m',
  cyan: '\x1b[36m',
  red: '\x1b[31m',
  dim: '\x1b[2m',
};

function log(msg) { console.log(msg); }
function success(msg) { console.log(`${COLORS.green}✔${COLORS.reset} ${msg}`); }
function warn(msg) { console.log(`${COLORS.yellow}⚠${COLORS.reset} ${msg}`); }
function error(msg) { console.error(`${COLORS.red}✖${COLORS.reset} ${msg}`); }
function header(msg) { console.log(`\n${COLORS.bold}${COLORS.cyan}${msg}${COLORS.reset}`); }

function hasCmd(cmd) {
  try {
    const check = process.platform === 'win32' ? `where ${cmd}` : `which ${cmd}`;
    execSync(check, { stdio: 'ignore' });
    return true;
  } catch (_) {
    return false;
  }
}

function hasDir(dirPath) {
  try {
    return fs.existsSync(dirPath) && fs.statSync(dirPath).isDirectory();
  } catch (_) {
    return false;
  }
}

function copyRecursive(src, dest, dryRun = false) {
  if (!fs.existsSync(src)) return;
  const stat = fs.statSync(src);
  if (stat.isDirectory()) {
    if (!dryRun) fs.mkdirSync(dest, { recursive: true });
    for (const file of fs.readdirSync(src)) {
      copyRecursive(path.join(src, file), path.join(dest, file), dryRun);
    }
  } else {
    if (!dryRun) {
      fs.mkdirSync(path.dirname(dest), { recursive: true });
      fs.copyFileSync(src, dest);
    }
  }
}

function removeRecursive(targetPath, dryRun = false) {
  if (fs.existsSync(targetPath)) {
    if (!dryRun) {
      fs.rmSync(targetPath, { recursive: true, force: true });
    }
    return true;
  }
  return false;
}

// Target coding agent definitions
const AGENTS = [
  {
    id: 'antigravity',
    label: 'Google Antigravity (IDE & 2.0 / CLI)',
    dirs: [
      path.join(HOME, '.gemini', 'antigravity', 'skills', 'idea-scout'),
      path.join(HOME, '.gemini', 'config', 'skills', 'idea-scout'),
      path.join(HOME, '.gemini', 'antigravity-cli', 'skills', 'idea-scout')
    ],
    detect: () => hasDir(path.join(HOME, '.gemini')) || hasCmd('agy') || hasCmd('antigravity'),
    instruction: 'Activate using `/scout` or type "scout this idea"'
  },
  {
    id: 'claude',
    label: 'Claude Code',
    dirs: [
      path.join(HOME, '.claude', 'skills', 'idea-scout')
    ],
    detect: () => hasCmd('claude') || hasDir(path.join(HOME, '.claude')),
    instruction: 'Type `/scout` or "investigate this concept"'
  },
  {
    id: 'hermes',
    label: 'Hermes Agent',
    dirs: [
      process.env.HERMES_HOME ? path.join(process.env.HERMES_HOME, 'skills', 'idea-scout') : path.join(HOME, '.hermes', 'skills', 'idea-scout')
    ],
    detect: () => hasCmd('hermes') || hasDir(path.join(HOME, '.hermes')),
    instruction: 'Loaded into native agent skills on start'
  },
  {
    id: 'openclaw',
    label: 'OpenClaw',
    dirs: [
      path.join(HOME, '.openclaw', 'workspace', 'skills', 'idea-scout'),
      path.join(HOME, '.openclaw', 'skills', 'idea-scout')
    ],
    detect: () => hasCmd('openclaw') || hasDir(path.join(HOME, '.openclaw')),
    instruction: 'Available in workspace skills registry'
  },
  {
    id: 'codex',
    label: 'Codex CLI',
    dirs: [
      path.join(HOME, '.codex', 'skills', 'idea-scout')
    ],
    detect: () => hasCmd('codex') || hasDir(path.join(HOME, '.codex')),
    instruction: 'Use `/scout <concept>`'
  },
  {
    id: 'cursor',
    label: 'Cursor',
    dirs: [
      path.join(HOME, '.cursor', 'skills', 'idea-scout')
    ],
    detect: () => hasCmd('cursor') || hasDir(path.join(HOME, '.cursor')),
    instruction: 'Invoke with `/scout` or in Composer chat'
  },
  {
    id: 'windsurf',
    label: 'Windsurf',
    dirs: [
      path.join(HOME, '.codeium', 'windsurf', 'skills', 'idea-scout')
    ],
    detect: () => hasCmd('windsurf') || hasDir(path.join(HOME, '.codeium', 'windsurf')),
    instruction: 'Prompt Cascade with "scout idea: <concept>"'
  },
  {
    id: 'cline',
    label: 'Cline / Roo Code',
    dirs: [
      path.join(HOME, '.cline', 'skills', 'idea-scout'),
      path.join(HOME, '.roo', 'skills', 'idea-scout')
    ],
    detect: () => hasDir(path.join(HOME, '.cline')) || hasDir(path.join(HOME, '.roo')),
    instruction: 'Type "use skill idea-scout"'
  },
  {
    id: 'aider',
    label: 'Aider',
    dirs: [
      path.join(HOME, '.aider', 'skills', 'idea-scout')
    ],
    detect: () => hasCmd('aider') || hasDir(path.join(HOME, '.aider')),
    instruction: 'Referenced via conventions'
  }
];

// Determine package root containing SKILL.md
function findSourceRoot() {
  const candidates = [
    path.resolve(__dirname, '..'),
    path.resolve(__dirname, '../..'),
    CWD,
  ];
  for (const dir of candidates) {
    if (fs.existsSync(path.join(dir, 'SKILL.md'))) {
      return dir;
    }
  }
  return null;
}

function parseArgs(args) {
  const opts = {
    all: false,
    dryRun: false,
    uninstall: false,
    list: false,
    workspace: false,
    only: null,
    help: false
  };

  for (let i = 0; i < args.length; i++) {
    const a = args[i];
    if (a === '--all' || a === '-a') opts.all = true;
    else if (a === '--dry-run' || a === '-d') opts.dryRun = true;
    else if (a === '--uninstall' || a === '-u') opts.uninstall = true;
    else if (a === '--list' || a === '-l') opts.list = true;
    else if (a === '--workspace' || a === '-w') opts.workspace = true;
    else if (a === '--only' || a === '-o') {
      opts.only = args[++i];
    } else if (a === '--help' || a === '-h') opts.help = true;
  }
  return opts;
}

function showHelp() {
  log(`
${COLORS.bold}🔭 Idea Scout — 1-Command Universal Skill Installer${COLORS.reset}

${COLORS.bold}USAGE:${COLORS.reset}
  node bin/install.js [options]
  bash install.sh [options]
  curl -fsSL https://raw.githubusercontent.com/${REPO}/main/install.sh | bash

${COLORS.bold}OPTIONS:${COLORS.reset}
  --all, -a            Install into ALL supported agent environments regardless of detection
  --only, -o <agent>   Install only to a specific agent (e.g. claude, antigravity, hermes, openclaw, codex)
  --workspace, -w      Install into current repository (.agents/skills/idea-scout)
  --dry-run, -d        Preview installation operations without writing files
  --uninstall, -u      Cleanly remove idea-scout from all detected agent skill directories
  --list, -l           List all supported agents and their local detection status
  --help, -h           Show this help message
`);
}

function run() {
  const opts = parseArgs(process.argv.slice(2));

  if (opts.help) {
    showHelp();
    process.exit(0);
  }

  header('🔭 Idea Scout — AI Agent Skill Installer');

  if (opts.list) {
    log('\nSupported AI Coding Agents:');
    for (const agent of AGENTS) {
      const detected = agent.detect() ? `${COLORS.green}[DETECTED]${COLORS.reset}` : `${COLORS.dim}[NOT DETECTED]${COLORS.reset}`;
      log(`  • ${agent.label.padEnd(38)} ${detected}`);
    }
    process.exit(0);
  }

  const sourceRoot = findSourceRoot();
  if (!sourceRoot && !opts.uninstall) {
    error('Could not find idea-scout source files (SKILL.md). Ensure you are running from the repository clone.');
    process.exit(1);
  }

  // Handle Uninstallation
  if (opts.uninstall) {
    header('Uninstalling Idea Scout from agents...');
    let uninstalledCount = 0;
    for (const agent of AGENTS) {
      for (const targetDir of agent.dirs) {
        if (fs.existsSync(targetDir)) {
          if (opts.dryRun) {
            log(`  [dry-run] would remove: ${targetDir}`);
          } else {
            removeRecursive(targetDir);
            success(`Removed from ${agent.label}: ${targetDir}`);
            uninstalledCount++;
          }
        }
      }
    }
    // Also workspace
    const wsDir = path.join(CWD, '.agents', 'skills', 'idea-scout');
    if (fs.existsSync(wsDir)) {
      if (opts.dryRun) log(`  [dry-run] would remove: ${wsDir}`);
      else {
        removeRecursive(wsDir);
        success(`Removed from workspace: ${wsDir}`);
        uninstalledCount++;
      }
    }
    log(`\n${COLORS.green}✔ Uninstallation complete (${uninstalledCount} locations cleaned).${COLORS.reset}`);
    process.exit(0);
  }

  // Determine Targets
  let targets = [];
  if (opts.only) {
    const target = AGENTS.find(a => a.id.toLowerCase() === opts.only.toLowerCase());
    if (!target) {
      error(`Unknown agent: '${opts.only}'. Run with --list to see supported agents.`);
      process.exit(1);
    }
    targets = [target];
  } else if (opts.all) {
    targets = AGENTS;
  } else {
    // Auto-detect installed agents
    targets = AGENTS.filter(a => a.detect());
  }

  if (targets.length === 0 && !opts.workspace) {
    warn('No supported AI coding agents detected automatically.');
    log(`  Run with ${COLORS.cyan}--all${COLORS.reset} to install to all agent directories anyway,`);
    log(`  or use ${COLORS.cyan}--only <id>${COLORS.reset} (e.g. claude, antigravity, hermes, openclaw, codex).`);
    log(`  Run with ${COLORS.cyan}--list${COLORS.reset} to view agent detection states.`);
    process.exit(0);
  }

  const itemsToCopy = [
    'SKILL.md',
    'registry.json',
    'references',
    'examples',
    'scripts'
  ];

  let installedTotal = 0;

  header(`Installing Idea Scout (${opts.dryRun ? 'DRY-RUN' : 'LIVE'})...`);

  for (const agent of targets) {
    log(`\n${COLORS.bold}→ ${agent.label}${COLORS.reset}`);
    for (const targetDir of agent.dirs) {
      if (opts.dryRun) {
        log(`  ${COLORS.dim}[dry-run] would copy skill package to: ${targetDir}${COLORS.reset}`);
      } else {
        fs.mkdirSync(targetDir, { recursive: true });
        for (const item of itemsToCopy) {
          const srcPath = path.join(sourceRoot, item);
          const destPath = path.join(targetDir, item);
          copyRecursive(srcPath, destPath, false);
        }
        success(`Installed to: ${targetDir}`);
        installedTotal++;
      }
    }
    log(`  ${COLORS.dim}How to run: ${agent.instruction}${COLORS.reset}`);
  }

  // Workspace install if requested or in git repo
  if (opts.workspace || targets.length === 0) {
    const wsTarget = path.join(CWD, '.agents', 'skills', 'idea-scout');
    log(`\n${COLORS.bold}→ Current Workspace (.agents/skills)${COLORS.reset}`);
    if (opts.dryRun) {
      log(`  ${COLORS.dim}[dry-run] would copy skill package to: ${wsTarget}${COLORS.reset}`);
    } else {
      fs.mkdirSync(wsTarget, { recursive: true });
      for (const item of itemsToCopy) {
        copyRecursive(path.join(sourceRoot, item), path.join(wsTarget, item), false);
      }
      success(`Installed to workspace: ${wsTarget}`);
      installedTotal++;
    }
  }

  log(`\n${COLORS.bold}${COLORS.green}✔ Done! Installed Idea Scout to ${installedTotal} destination(s).${COLORS.reset}`);
  log(`\nTry it now in your agent:`);
  log(`  ${COLORS.cyan}/scout "speculative tree decoding"${COLORS.reset}`);
  log(`  ${COLORS.cyan}scout this idea: local-first SQLite sync with CRDTs${COLORS.reset}\n`);
}

run();
