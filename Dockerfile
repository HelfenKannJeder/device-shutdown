FROM python:3.9.1-buster
WORKDIR /usr/src/app
COPY . .
CMD [ "python", "./shutdown.py" ]
