FROM alpine
#ENV to test the python code
ENV TRAVIS_PULL_REQUEST true
ENV TRAVIS_BRANCH prod
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
#CMD for testing purpose
CMD echo "TRAVIS_PULL_REQUEST is $TRAVIS_PULL_REQUEST"
CMD echo "TRAVIS_BRANCH is $TRAVIS_BRANCH"
CMD ["git diff --name-only HEAD...master"]
ENTRYPOINT ["/kb-docker/script.sh"]
