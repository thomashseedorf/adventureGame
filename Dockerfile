# syntax=docker/dockerfile:1
FROM python:3.8-alpine
COPY ./requirements.txt /adventuregame/requirements.txt
WORKDIR /adventuregame
RUN apk add --no-cache bash coreutils grep sed
RUN pip install -r requirements.txt
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENTRYPOINT [ "flask"]
CMD [ "run", "--host", "0.0.0.0" ]
