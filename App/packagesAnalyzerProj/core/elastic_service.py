from packagesAnalyzerProj import settings
from elasticsearch import Elasticsearch, TransportError

import logging

logger = logging.getLogger(__name__)

def get_client():
    return Elasticsearch(settings.ES_HOST+':'+settings.ES_PORT)

    '''
     code below is commented because of:
        Dockerfile-ElasticSearch.Dockerfile file with line:
        HEALTHCHECK CMD curl -XPUT  'localhost:9200/elastic_packages_tree?pretty' | grep -E '^green'

        will make index on setup
    '''
    # es= Elasticsearch(settings.ES_HOST+':'+settings.ES_PORT)
    # # ignore 400 cause by IndexAlreadyExistsException when creating an index
    # es.indices.create(index='elastic_packages_tree', ignore=400)
    # #The ignore=400 arg is an interim solution here for the Python client. The code above will create index if it doesn't exist, and won't raise an error if it is already there.
    # print(f' \n settings.ES_HOST: {settings.ES_HOST}, settings.ES_PORT: {settings.ES_PORT}  \n ')
    # return es

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
    # doc_type= "package_tree_type"
    client = get_client()
    response = client.update(
        settings.ES_INDEX,
        id = tree_dic['id'],
        # id = tree_dic['npm_name'],  or this didnt decide yet
        body = {
             doc_type : tree_dic,
            'doc_as_upsert':True,         
        }
    )
    return response

def get_packages_tree_count():
    client = get_client()
    client.indices.refresh(settings.ES_INDEX)
    return client.cat.count(settings.ES_INDEX, params={"format": "json"})

def get_top_most_hits():
    """
        will return 10 top hits, unless provides otherwise 
    """

    
    client =  get_client()
    result = client.search(index=settings.ES_INDEX )

    #return result
    #print(f' \n  result : {result}  \n')

    a = result['hits']['hits']
    # print(f' result: \n {a}')

    #return a

    list_r = []
    for h in result['hits']['hits']:
        #b= h['_source']
        print(h['_source']['npm_name'])
        list_r.append(h['_source']['npm_name'])

    print(f'list_r : {list_r}' )
    return {'list_r': list_r}

