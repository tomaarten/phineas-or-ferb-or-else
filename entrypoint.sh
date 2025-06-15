#!/usr/bin/env bash
set -euo pipefail

mkdir -p /app/data
# Download model if missing
[ -f /app/data/model.tflite ] && echo "Model exists" \
  || wget -q -O /app/data/model.tflite https://raw.githubusercontent.com/tomaarten/phineas-or-ferb-or-else/main/model.tflite

# Initialize results file
touch /app/data/results.json

exec python server.py
