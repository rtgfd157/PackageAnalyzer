FROM ubuntu 

# not using node because of problem with react-loader. need to force or --legacy-peer-deps

RUN mkdir /frontend
RUN  apt-get update
RUN DEBIAN_FRONTEND="noninteractive" apt-get -y install tzdata
RUN  yes | apt-get install nodejs

RUN  yes | apt-get install npm


# https://stackoverflow.com/questions/30716937/dockerfile-build-possible-to-ignore-error
# RUN  npm i -g @vue/cli  2>&1 > install_docker.log || echo "There were failing in npm i -g @vue/cli  !"


WORKDIR /frontend

# install app dependencies
COPY package.json .
COPY package-lock.json .
RUN npm install --save 
RUN npm install react-scripts@3.4.1 -g  --save

# libraries used in project. somehow package.json dont install them ...
RUN npm install react-loader@2.4.7 bootstrap@5.1.0 react-router-dom@5.2.0 reactstrap@8.9.0 --save 

# add app
COPY . .

CMD ["npm", "start" ]
