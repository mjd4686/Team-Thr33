FROM python:3.6.6-stretch
ENV PYTHONUNBUFFERED 1
EXPOSE 8000

ADD ./project ./
ADD ./requirements.txt ./

RUN apt-get update
RUN apt-get install -y apt-utils libyaml-dev python3-dev libpython-dev

#RUN pip install pyyaml==3.12

#RUN wget

RUN pip install -r requirements.txt

ADD ./start.sh ./

CMD ./start.sh 
