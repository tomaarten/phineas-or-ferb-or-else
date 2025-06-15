FROM python:3.9-slim

WORKDIR /app

# System dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libjpeg-dev \
    curl \
    zlib1g-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app source
COPY . .
COPY templates/ templates/
# keep a copy of the bundled model so volumes can't overwrite it
RUN cp model.tflite default_model.tflite

# run setup script before launching the application
CMD ["bash", "-c", "python setup_paths.py && python app.py"]
