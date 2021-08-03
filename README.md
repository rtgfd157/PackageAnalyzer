
# Package Analyzer Project:

The project will search for package in npmjs and will insert to DB.
Each package will show also his dependency.

Stack: Docker - Postgres -  Celery - Django  - React - Flower

need to have:
Docker and Docker compose

Initalize project:  
sudo docker-compose -f "docker-compose.yml" up -d --build


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
- ~~good looking UI~~ added colors. more search being made message in when taking long to build long tree api from web.  
- optimise adding to model
- refine code so it will be fit for diffrent languages libraries (pipy - python, nugat-c#  and more.....)
- Caching with elasticsearch. search hierarcy: 1)caching- elasticsearch 2) DB 3) api call/scraping 
- security for password in production
- website data coruption- when runing task could be situation of all db ruin if the website destionation will decide to change there package data answering.
- block searching all  Npm Packages in Back end
- logging on DB or on file
- async function fetch on Front end. 
- Functionality _**Error**_ when: searching for "api" keyword, then python _**Error**_ because recursive is too deep.  message -   RecursionError: maximum recursion depth exceeded while calling a Python object.
