$ErrorActionPreference = "Stop"

$root = Split-Path -Parent $PSScriptRoot
$venvPython = Join-Path $PSScriptRoot ".venv\Scripts\python.exe"
$venvMkdocs = Join-Path $PSScriptRoot ".venv\Scripts\mkdocs.exe"
$requirements = Join-Path $PSScriptRoot "requirements.txt"
$config = Join-Path $PSScriptRoot "mkdocs.yml"

if (-not (Test-Path $venvPython)) {
    python -m venv (Join-Path $PSScriptRoot ".venv")
}

& $venvPython -m pip install -r $requirements
& $venvMkdocs serve -f $config
