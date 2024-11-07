# Build stage
FROM python:3.12-slim-bookworm AS builder

WORKDIR /app

# Install git for pip requirements
RUN apt-get update && apt-get install -y --no-install-recommends git \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt \
    && pip install --no-cache-dir git+https://github.com/AnthonyBloomer/tmdbv3api.git

# Final stage
FROM python:3.12-slim-bookworm

LABEL maintainer="xpl0r3the4byss" \
      support=https://github.com/xpl0r3the4byss/xpl0r3-plex-utills \
      discord=https://discord.gg/z3FYhHwHMw

# Install system dependencies
RUN apt-get update && apt-get upgrade -y \
    && apt-get install -y --no-install-recommends \
        wget \
        mediainfo \
        nginx \
        ffmpeg \
        libsm6 \
        libxext6 \
        nano \
    && rm -rf /var/lib/apt/lists/*

# Copy Python packages from builder
COPY --from=builder /usr/local/lib/python3.12/site-packages/ /usr/local/lib/python3.12/site-packages/
COPY --from=builder /usr/local/bin/ /usr/local/bin/

WORKDIR /app

# Copy application files
COPY ./app ./app
COPY ./main.py .
COPY ./version .
COPY ./start.sh .
COPY app/static/dockerfiles/default /etc/nginx/sites-enabled/default

# Set permissions
RUN chmod +x start.sh

# Set timezone
ARG TZ=Europe/London
ENV TZ="${TZ}"

# Security headers for nginx
RUN echo "add_header X-Frame-Options SAMEORIGIN;" >> /etc/nginx/conf.d/security.conf \
    && echo "add_header X-Content-Type-Options nosniff;" >> /etc/nginx/conf.d/security.conf \
    && echo "add_header X-XSS-Protection \"1; mode=block\";" >> /etc/nginx/conf.d/security.conf \
    && echo "add_header Content-Security-Policy \"default-src 'self';\";" >> /etc/nginx/conf.d/security.conf

EXPOSE 80 5000

VOLUME [ "/films", "/config", "/logs" ]

CMD ["/app/start.sh"]
