# Use a more current, slim Python base
FROM python:3.09-slim

# Set working directory
WORKDIR /app

# 1. Install system dependencies and clean up
RUN apt-get update \
 && apt-get install -y --no-install-recommends \
      build-essential \
      libjpeg-dev \
      curl \
      zlib1g-dev \
 && rm -rf /var/lib/apt/lists/*

# 2. Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 3. Copy application code and entrypoint
COPY app/ ./app/
COPY entrypoint.sh ./entrypoint.sh
RUN chmod +x entrypoint.sh

# 4. Bake in a fallback model in case runtime download fails
COPY model.tflite ./default_model.tflite

# 5. Expose the application port
EXPOSE 5000

# 6. Use entrypoint to prepare environment and launch
ENTRYPOINT ["./entrypoint.sh"]
CMD ["python", "app.py"]
