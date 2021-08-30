FROM python:3.8-slim-buster

WORKDIR /app

COPY ./ .

RUN pip3 install -r requirements.txt

# CMD ["ls"]

# CMD flask run --host=0.0.0.0
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]

# FROM python:3-alpine

# WORKDIR /app

# RUN apk add --update --no-cache g++ gcc libxslt-dev

# COPY ./ .

# RUN pip3 install -r requirements.txt

# CMD ["ls"]