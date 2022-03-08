FROM python:3.9-slim

RUN addgroup --system app && adduser --system --group app

USER app

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["python", "main.py"]