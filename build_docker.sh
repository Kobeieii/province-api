#!/bin/bash

DATE=`date +%Y.%m.%d.%H.%M`
NAME=province_api

echo "Container exists"
docker container rm -f $NAME
echo "Deleted the existing docker container"

echo "image exists"
docker rmi -f $NAME

echo "build the docker image"
docker build -t $NAME .

echo "Deploying the updated container"
docker run -d -p 80:80 --name $NAME --restart always $NAME

echo "Deploying the container"