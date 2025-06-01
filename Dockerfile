FROM python:3-alpine

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
COPY templates/ templates/

CMD ["python", "app.py"]
