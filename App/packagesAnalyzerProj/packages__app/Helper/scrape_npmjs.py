import requests
import subprocess
import sys
#from packages__app.models import NpmPackage, NpmPackageDependecy
import json

def get_page_resource( search_word):
    res = requests.get(f'https://registry.npmjs.org/{search_word}/latest')
    if res.status_code != 200:
        print(f' \n api not avaialable https://registry.npmjs.org/{search_word}/latest  - status code: {res.status_code}')
        return None
    else:
        return res



def start_scraping_npmjs_for_package(search_word):
    """
    scrape for keyword
    """
    res = get_page_resource( search_word)
    if res == None: return None

    ret_dic = {}

    try:
        dic = res.json()

        # if dic.get() not found is return None
        ret_dic['package_ver']= dic.get('version') 
        ret_dic['dependencies']= dic.get('dependencies')
        ret_dic['number_of_maintainers']= len(dic.get('maintainers'))
        ret_dic['unpackedSize']= dic.get('dist').get('unpackedSize')
        ret_dic['license']= dic.get('license')
        #print(f' \n ^^^^^^^ \n { dic.get("dist").get("unpackedSize")} \n ')
        return ret_dic
        
    except:
        return None
  


def start_npm_registry_fetch_for_package_security(search_word,version):
    process = subprocess.Popen(['node', 'npm_fetch_sec.js', search_word, version],
                     stdout=subprocess.PIPE, 
                     stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()

    try:
        stdout_utf = stdout.decode("utf8")
        stdout_utf = json.loads(stdout_utf) 
    except:
        stdout_utf = None
    
    try:
        stderr_utf = stderr.decode("utf8")
        stderr_utf = json.loads(stderr_utf) 
    except:
        stderr_utf = None

    return stdout_utf , stderr_utf
    

def  returning_dic_from_pack_security_dic(search_word,version):

    dic = start_npm_registry_fetch_for_package_security(search_word,version)

    ret_dic = {}

    try:

        if len (dic[0].get('actions')) > 0:
            ret_dic['is_exploite'] =True
            ret_dic['num_low_severity'] = dic[0].get('metadata').get('vulnerabilities').get('low')
            ret_dic['num_moderate_severity'] =  dic[0].get('metadata').get('vulnerabilities').get('moderate')
            ret_dic['num_high_severity'] =   dic[0].get('metadata').get('vulnerabilities').get('high') 
            ret_dic['num_critical_severity'] =  dic[0].get('metadata').get('vulnerabilities').get('critical')
            ret_dic['num_info_severity'] =  dic[0].get('metadata').get('vulnerabilities').get('info')  

        else:
            ret_dic['is_exploite'] =False
        
        #print (f' ret_dic: {ret_dic} ')
        return ret_dic
        
    except :
        print("Unexpected error:", sys.exc_info()[0])

        print (f'  -- ret_dic: {ret_dic} ')
        return None

    


    

    