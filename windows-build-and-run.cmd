:: Stopping running containters
ECHO "---stopping container----"
docker stop kaffeeklatsch

ECHO "---removing stale images----"
docker image prune -f

ECHO "---removing stopped containers----"
docker container prune -f

:: Build new containter
ECHO Building docker containter...
docker build -t cmsc-495-project .

:: Run new containter
ECHO Running new container...
docker run --rm -it -p 5000:5000 --name kaffeeklatsch cmsc-495-project