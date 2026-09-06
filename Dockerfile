# ================================================
# File-Store-Pro — Dockerfile
# Made by: botifyx-bots | @BotifyX_Pro_Botz
# Supports: Heroku · Render · VPS · Local
# ------------------------------------------------
# Before deploying, edit config.py with your values
# ================================================

FROM python:3.11-slim-bookworm

LABEL maintainer="botifyx-bots"

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /app

# Fixed - bookworm repos (bullseye is EOL = 404 error)
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    g++ \
    libffi-dev \
    libssl-dev \
    curl \
    git \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

COPY . .

# Render gives dynamic PORT, so use $PORT
EXPOSE 10000

# Remove healthcheck for Render - Render has its own
# HEALTHCHECK removed

CMD ["python3", "main.py"]
