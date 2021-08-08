from packagesAnalyzerProj import settings
from elasticsearch import Elasticsearch, TransportError

import logging

logger = logging.getLogger(__name__)

def get_client():

    es= Elasticsearch(settings.ES_HOST+':'+settings.ES_PORT)
    # ignore 400 cause by IndexAlreadyExistsException when creating an index
    es.indices.create(index='elastic_packages_tree', ignore=400)
    #The ignore=400 arg is an interim solution here for the Python client. The code above will create index if it doesn't exist, and won't raise an error if it is already there.
    print(f' \n settings.ES_HOST: {settings.ES_HOST}, settings.ES_PORT: {settings.ES_PORT}  \n ')
    return es

def el_search_for_package_tree(query):
    client = get_client()
    #print(f' info : {client.info()}')  
    #print(f'client : {client}')
    result = client.search(index=settings.ES_INDEX, 
    body={
        'query':{
            'match':{
                'npm_name': query,
            },
        },
    })
    a = result['hits']['hits']
    # print(f' result: \n {a}')
    for h in result['hits']['hits']:
        #b= h['_source']
        return h['_source']
    return {}
        #print(f' ---  {b}   --- \n  ')
    #return(h['_source'] for h in result['hits']['hits'])

def upsert_tree_in_el_search(tree_dic):
    # document type (string)
    doc_type= "doc"
    client = get_client()
    response = client.update(
        settings.ES_INDEX,
        id = tree_dic['npm_name'],
        body = {
             doc_type : tree_dic,
            'doc_as_upsert':True,         
        }
    )
    return response

