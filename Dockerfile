FROM python:3.12-slim-bookworm

ENV PYTHONDONTWRITEBYTCODE=1 \
PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update && apt-get install -y \
    gcc \
    build-essential \
    libpq-dev \
    libffi-dev \
    curl \
    libssl-dev \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*


COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt


COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

COPY . .

EXPOSE 8000


COPY build.sh ./build.sh

RUN chmod +x ./build.sh

CMD ["./build.sh"]
