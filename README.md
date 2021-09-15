
# Package Analyzer Project:

**Notice:**  
**calling links such npmjs https://registry.npmjs.org/keyword/latest is being Throttling by them, so when doing search write package with little dependecies ...**



### Remote Npmjs API/Scraping:  
**Best approach is to Clone whole NPM metadata DB server with IT tools**
we have api call limit. so, i wont add threading when scraping, or if i will add it will be a few (and none recursivly).     

## Part 1:
[Npm Package Tree Search](README/README_1.md)

## Part 2:
[Npm security](README/README_2.md)

Stack: Docker - Postgres -  Celery - Django  - React - Flower - ElasticSearch

need to have:
Docker and Docker compose

Initalize project:  
sudo docker-compose -f "docker-compose.yml" up -d --build  
Note:
dont build if data directory exists. could be acheived with : sudo rm -rf data  

 
From web browser:  
 Front end:   
    http://127.0.0.1:3000/

 Backend( rest framework):   
    http://127.0.0.1:8000/

 flower:  
    http://127.0.0.1:5555/

  ElasticSearch:   
    http://127.0.0.1:9200/
