#!/bin/bash
ADDRESS=gcr.io
PROJECT_ID=burner-nitkumar27
REPOSITORY=burner-nitkumar27
VERSION=3.0

docker build -t burner-nitkumar27:${VERSION} .


docker tag burner-nitkumar27:${VERSION} $ADDRESS/${PROJECT_ID}/${REPOSITORY}:${VERSION}

docker push $ADDRESS/${PROJECT_ID}/${REPOSITORY}:${VERSION}
