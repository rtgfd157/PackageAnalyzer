import requests

#from packages__app.models import NpmPackage, NpmPackageDependecy
import json

def get_page_resource( search_word):
    res = requests.get(f'https://registry.npmjs.org/{search_word}/latest')
    if res.status_code != 200:
        print(f' \n api not avaialable https://registry.npmjs.org/{search_word}/latest  - status code: {res.status_code}')
        return None
    else:
        return res



def start_scraping_npmjs_for_package_dependencies(search_word):
    """
    scrape for keyword
    """
    res = get_page_resource( search_word)
    if res == None: return None

    try:
        dic = res.json()
        dependencies= dic.get('dependencies')
        return dependencies
    except:
        return None



def start_scraping_npmjs_for_package(search_word):
    """
    scrape for keyword
    """
    res = get_page_resource( search_word)
    if res == None: return None

    try:
        dic = res.json()
        package_ver= dic.get('version')
        
        return package_ver
        
    except:
        return None
  




    


    

    