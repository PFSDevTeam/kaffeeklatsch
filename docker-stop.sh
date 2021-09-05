#!/bin/sh

printf "\n\n---stopping container----\n\n"
docker stop kaffeeklatsch

printf "\n\n---removing stale images----\n\n"
docker image prune -f

printf "\n\n---removing stopped containers----\n\n"
docker container prune -f