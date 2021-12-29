FROM python:3.8

COPY ./web/ /web/

WORKDIR /web

EXPOSE 8000/tcp

RUN apt-get update && apt-get upgrade -y && \
    pip install --upgrade pip && pip install --no-cache-dir -r /web/requirements.txt

ENTRYPOINT ["sh", "./entrypoint.sh"]
