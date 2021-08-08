
# Package Analyzer Project:

The project will search for package in npmjs and will insert to DB.
Each package will show also his dependency.

Stack: Docker - Postgres -  Celery - Django  - React - Flower - ElasticSearch

need to have:
Docker and Docker compose

Initalize project:  
sudo docker-compose -f "docker-compose.yml" up -d --build

~~In elasticsearch container:
in shell post ->   
 curl -XPUT 'localhost:9200/elastic_packages_tree?pretty'  
The command will make index (that will correlate to index in settings file)~~ 
checking every  search in code and create if not exists, need to change to make on server restart, or on elasticsearch image built.   



From web browser:  
 Front end: 
    http://127.0.0.1:3000/

 Backend( rest framework): 
    http://127.0.0.1:8000/

 flower: 
    http://127.0.0.1:5555/



need to add:

- ~~Full recursive tree view - Front end~~ - Done    
- tests
- ~~periodic celery task. currently by url call:~~
 http://127.0.0.1:8000/celery_task_updating_npm_packages_and_dependecies and also periodically(timing in our setting py file )  
- split db and call for api by threading.
- ~~good looking UI added colors. need to add:  search being made message  when in searching process.~~
with:  https://steemit.com/utopian-io/@jfuenmayor96/show-a-loading-animation-while-your-elements-are-loading-in-react
- optimise adding to model 
- refine code so it will be fit for diffrent languages libraries (pipy - python, nugat-c#  and more.....)
- Caching with elasticsearch. search hierarcy: 1)caching- elasticsearch 2) DB 3) api call/scraping 
- security for password in production - (not matter now)
- website data coruption- when runing task could be situation of all db ruin if the website destionation will decide to change there package data answering.
- ~~block searching all  Npm Packages in Back end - to change from viewsets in packages__app/api/view ...~~( not matter now)
- logging on DB or on file
- ~~async function fetch on Front end.~~ 

