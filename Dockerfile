FROM python:3.8-slim

# update apt-get
RUN apt-get update -y && apt-get upgrade -y && apt-get install vim lsof git curl sudo -y && pip install pipenv
