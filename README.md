# A Docker image for validating and deploying Knowledge Base Articles

## Table of Contents

-   [Overview]
-   [Quickstart]
-   [Handbooks]

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


[Overview]: https://github.com/pivotal-gss/pcf-guide#overview
[Architecture]: https://github.com/pivotal-gss/pcf-guide#architecture
[Handbooks]: https://github.com/pivotal-gss/pcf-guide#development
