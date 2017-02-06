FROM alpine
RUN apk add --update \
    python \
    python-dev \
    py-pip \
    build-base \
    gcc \
    bash \
    git \
  && rm -rf /var/cache/apk/*
RUN pip install --upgrade pip
RUN git clone https://github.com/pivotal-gss/kb-docker.git
WORKDIR /kb-docker
RUN pip install -r /kb-docker/requirements.txt

EXPOSE 8080
ENTRYPOINT ["/kb-docker/script.sh"]
