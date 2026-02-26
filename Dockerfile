FROM python:3.10-slim

WORKDIR /app

COPY scientific-calc/ .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "app.py"]
