$ErrorActionPreference = "Stop"

$RepositoryRoot = Split-Path -Parent $PSScriptRoot
$VirtualEnvPython = Join-Path $RepositoryRoot ".venv\Scripts\python.exe"
$Python = if (Test-Path -LiteralPath $VirtualEnvPython) { $VirtualEnvPython } else { "python" }

& $Python (Join-Path $PSScriptRoot "validate.py")
exit $LASTEXITCODE
