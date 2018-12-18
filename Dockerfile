FROM python:3.6.6-stretch
ENV PYTHONUNBUFFERED 1
EXPOSE 8000

ADD ./requirements.txt ./

RUN apt-get update
RUN apt-get install -y apt-utils libyaml-dev python3-dev libpython-dev

RUN pip install -r requirements.txt

ADD ./project ./
ADD ./start.sh ./

CMD ./start.sh 
