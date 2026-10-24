#!/usr/bin/env bash
# Optional local checklist before submitting your commit SHA to UBLearns.
set -euo pipefail

ROOT="$(cd "$(dirname "$0")" && pwd)"
cd "$ROOT"

fail=0

require_file() {
  if [[ ! -f "$1" ]]; then
    echo "MISSING: $1"
    fail=1
  else
    echo "OK: $1"
  fi
}

echo "Lab 1 submit check"
echo "------------------"

require_file "tools.py"
require_file "agent.py"
require_file "run_examples.py"
require_file "design_note.md"
require_file "README.md"
require_file "requirements.txt"

# At least some logs present
shopt -s nullglob
success_logs=(logs/success_*.txt)
failure_logs=(logs/failure_*.txt)
if ((${#success_logs[@]} < 3)); then
  echo "MISSING: need at least 3 files matching logs/success_*.txt (found ${#success_logs[@]})"
  fail=1
else
  echo "OK: ${#success_logs[@]} success log(s)"
fi
if ((${#failure_logs[@]} < 2)); then
  echo "MISSING: need at least 2 files matching logs/failure_*.txt (found ${#failure_logs[@]})"
  fail=1
else
  echo "OK: ${#failure_logs[@]} failure log(s)"
fi

if git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  if [[ -n "$(git status --porcelain)" ]]; then
    echo "WARN: working tree has uncommitted changes — commit before taking the SHA."
  fi
  echo "Current HEAD: $(git rev-parse HEAD)"
else
  echo "WARN: not a git repository yet."
fi

if [[ "$fail" -ne 0 ]]; then
  echo "------------------"
  echo "Submit check FAILED. Fix the items above, then re-run."
  exit 1
fi

echo "------------------"
echo "Submit check PASSED (local file checklist only)."
echo "Next: push, run git rev-parse HEAD, paste the SHA into UBLearns."
