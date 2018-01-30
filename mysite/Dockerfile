FROM python:2.7

ENV PYTHONUNBUFFERED 1

ADD requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt --no-cache-dir

ADD . /app
WORKDIR /app

CMD ./run.sh
