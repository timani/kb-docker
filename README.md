# Docker image for validating and deploying Knowledge Base Articles

A small Docker image to validate and build articles so they can be validated and published to the Pivotal Knowledge Base. For more information on how to build and customize the image, review the [Documentation].

## Table of Contents

-   [Overview]
-   [Quickstart]
-   [Developers]

## Overview

Get the stack (only once):

```
git clone https://github.com/pivotal-gss/kb-docker.git
cd kb-docker
# This organization does not exist on Docker Hub yet
docker pull pivotal-support/kb-docker
```

## Quickstart

### Run your stack: 

```
docker run ...

```

Show me the logs:

```
docker logs ...
```

Stop it:

```
docker stop ...
```

Update it:

```
# Get the latest image from source
git pull
# Update the docker image
docker pull pivotal-support/kb-docker
```

## Developers

Some information about how to develop and customize the Docker image. 

[Overview]: https://github.com/pivotal-gss/pcf-guide#overview
[Documentation]: https://github.com/pivotal-gss/kb-docker/tree/master/docs
[Quickstart]: https://github.com/pivotal-gss/pcf-guide#architecture
[Handbooks]: https://github.com/pivotal-gss/pcf-guide#development
