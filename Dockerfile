FROM ubuntu 
ENV PYTHONUNBUFFERED 1
RUN mkdir /App
RUN  apt-get update
RUN DEBIAN_FRONTEND="noninteractive" apt-get -y install tzdata
RUN  yes | apt-get install python
# RUN  yes | apt-get install python3-dev default-libmysqlclient-dev build-essential
RUN   yes |  apt-get install  python-dev libpq-dev postgresql postgresql-contrib
RUN  yes |apt-get install python3-pip


# https://stackoverflow.com/questions/30716937/dockerfile-build-possible-to-ignore-error
# RUN  npm i -g @vue/cli  2>&1 > install_docker.log || echo "There were failing in npm i -g @vue/cli  !"
# RUN npm i -g @vue/cli


WORKDIR /App
COPY requirements.txt /App/
RUN pip3 install -r requirements.txt
COPY App /App/


WORKDIR App/packagesAnalyzerProj
