FROM python:3.11-alpine

# FIX: Swap apt-get out for alpine's apk package manager
RUN apk add --no-cache \
    gcc \
    musl-dev \
    postgresql-dev

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
