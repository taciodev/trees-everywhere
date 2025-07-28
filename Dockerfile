FROM python:3.11-slim-bullseye
LABEL maintainer="taciano.dev@outlook.com"

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt ./

RUN apt-get update && apt-get install -y --no-install-recommends \
    netcat-openbsd \
    gcc \
    libffi-dev \
    musl-dev && \
    pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt && \
    apt-get purge -y --auto-remove gcc libffi-dev musl-dev && \
    rm -rf /var/lib/apt/lists/*

COPY . .

RUN useradd --no-create-home duser && \
    chown -R duser:duser /app && \
    chmod +x /app/scripts/commands.sh

USER duser

EXPOSE 8000

CMD ["sh", "scripts/commands.sh"]
