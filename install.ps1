# 🔭 Idea Scout — Windows PowerShell 1-Command Installer
# Usage:
#   irm https://raw.githubusercontent.com/Its-Atharva-Gupta/idea-scout/main/install.ps1 | iex

$ErrorActionPreference = "Stop"

$Repo = "Its-Atharva-Gupta/idea-scout"
$Branch = "main"

# Check if Node is installed
if (-not (Get-Command node -ErrorAction SilentlyContinue)) {
    Write-Error "Node.js (>= 16) is required. Please install Node.js from https://nodejs.org"
    exit 1
}

# Check if running locally
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path -ErrorAction SilentlyContinue
if ($ScriptDir -and (Test-Path "$ScriptDir\bin\install.js")) {
    & node "$ScriptDir\bin\install.js" $args
    exit $LASTEXITCODE
}

# Remote execution
$TempDir = Join-Path $env:TEMP ("idea-scout-install-" + [Guid]::NewGuid().ToString("N"))
New-Item -ItemType Directory -Path $TempDir -Force | Out-Null

try {
    Write-Host "→ Fetching latest Idea Scout skill from GitHub ($Repo)..." -ForegroundColor Cyan
    if (Get-Command git -ErrorAction SilentlyContinue) {
        & git clone --depth 1 -b $Branch "https://github.com/$Repo.git" $TempDir 2>$null
    } else {
        $ZipPath = Join-Path $env:TEMP "idea-scout.zip"
        Invoke-WebRequest -Uri "https://github.com/$Repo/archive/refs/heads/$Branch.zip" -OutFile $ZipPath
        Expand-Archive -Path $ZipPath -DestinationPath $TempDir -Force
        $ExtractedFolder = Get-ChildItem -Path $TempDir | Where-Object { $_.PSIsContainer } | Select-Object -First 1
        Copy-Item -Path "$($ExtractedFolder.FullName)\*" -Destination $TempDir -Recurse -Force
        Remove-Item $ZipPath -Force -ErrorAction SilentlyContinue
    }

    & node "$TempDir\bin\install.js" $args
}
finally {
    Remove-Item -Path $TempDir -Recurse -Force -ErrorAction SilentlyContinue
}
