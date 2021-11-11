FROM python:3.9-bullseye

LABEL maintainer="JKirkcaldy"

WORKDIR /app
COPY ./app ./app
COPY ./main.py .
COPY ./requirements.txt .
COPY ./entrypoint.sh .
COPY ./start.sh .



# Install requirements

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 80
EXPOSE 5000
VOLUME [ "/films" ]
VOLUME [ "/config" ]
VOLUME [ "/logs" ]

RUN apt-get update && apt-get install -y supervisor mediainfo nginx \
&& rm -rf /var/lib/apt/lists/*
COPY supervisord-debian.conf /etc/supervisor/conf.d/supervisord.conf
COPY app/static/dockerfiles/default /etc/nginx/sites-enabled/default

ENV NGINX_MAX_UPLOAD 0
ENV NGINX_WORKER_PROCESSES 1
ENV LISTEN_PORT 80
RUN chmod +x start.sh
RUN chmod +x entrypoint.sh

ENV TZ=Europe/London

ENTRYPOINT ["/app/entrypoint.sh"]
CMD ["/app/start.sh"]
