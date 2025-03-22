FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY send_to_datadog.py .

CMD ["python", "send_to_datadog.py"]
