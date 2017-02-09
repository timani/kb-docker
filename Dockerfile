FROM alpine
#ENV to test the python code
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
ADD . /kb-docker
WORKDIR /kb-docker
# Should the dependencies be packakged as part of the repo?
# cases when pip is unavailable
# RUN pip install virtualenv
# RUN virtualenv venv
# RUN source venv/bin/activate
RUN pip2 install -r requirements.txt
ENTRYPOINT ["/kb-docker/script.sh"]
