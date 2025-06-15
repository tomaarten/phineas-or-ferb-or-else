#!/usr/bin/env bash
set -euo pipefail

MODEL_PATH=/app/model.tflite
# Download only if missing
if [ ! -f "$MODEL_PATH" ]; then
  echo "⏬ Retrieving model.tflite..."
  wget -q -O "$MODEL_PATH" "https://raw.githubusercontent.com/tomaarten/phineas-or-ferb-or-else/main/model.tflite"
  echo "✅ Download complete."
fi

# Launch your app (adjust as needed)
exec python server.py
