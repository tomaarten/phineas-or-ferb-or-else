import os
from pathlib import Path
import shutil

UPLOAD_DIR = Path('/app/static/uploads')
MODEL_PATH = Path(os.environ.get('MODEL_PATH', '/app/model.tflite'))
RESULTS_PATH = Path(os.environ.get('RESULTS_PATH', '/app/results.json'))
DEFAULT_MODEL = Path('/app/default_model.tflite')

# Ensure upload directory exists
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

# Ensure results file exists
if not RESULTS_PATH.exists():
    RESULTS_PATH.parent.mkdir(parents=True, exist_ok=True)
    RESULTS_PATH.write_text('{}')

# Ensure model file exists and is not empty
if not MODEL_PATH.exists() or MODEL_PATH.stat().st_size == 0:
    MODEL_PATH.parent.mkdir(parents=True, exist_ok=True)
    if DEFAULT_MODEL.exists():
        shutil.copy(DEFAULT_MODEL, MODEL_PATH)
