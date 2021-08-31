FROM ubuntu 
ENV PYTHONUNBUFFERED 1
RUN mkdir /App
WORKDIR /App
RUN  apt-get update
RUN DEBIAN_FRONTEND="noninteractive" apt-get -y install tzdata
RUN  yes | apt-get install python
# RUN  yes | apt-get install python3-dev default-libmysqlclient-dev build-essential
RUN   yes |  apt-get install  python-dev libpq-dev postgresql postgresql-contrib
RUN  yes |apt-get install python3-pip


# npm node and libraray for using  npm-registry-fetch in NpmSecurity model fetching info
RUN  yes | apt-get install nodejs
RUN  yes | apt-get install npm
RUN  yes | npm install npm-registry-fetch@11.0.0 --save 2>&1 > install_docker.log || echo "There were failing in npm i -g npm-registry-fetch  !"


# https://stackoverflow.com/questions/30716937/dockerfile-build-possible-to-ignore-error
# RUN  npm i -g @vue/cli  2>&1 > install_docker.log || echo "There were failing in npm i -g @vue/cli  !"
# RUN npm i -g @vue/cli


WORKDIR /App
COPY requirements.txt /App/
RUN pip3 install -r requirements.txt
COPY App /App/


WORKDIR App/packagesAnalyzerProj
