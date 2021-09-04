import requests
import subprocess
import sys
#from packages__app.models import NpmPackage, NpmPackageDependecy
import json

def get_page_resource( search_word, search_keyword_version):
    print(f'https://registry.npmjs.org/{search_word}/{search_keyword_version}')
    res = requests.get(f'https://registry.npmjs.org/{search_word}/{search_keyword_version}')
    print(f'res $$  - {res}')
    if res.status_code != 200:
        print(f' \n api not avaialable https://registry.npmjs.org/{search_word}/{search_keyword_version}  - status code: {res.status_code}')
        return None
    else:
        return res

def return_dic_dependencies_out_of_notallowed_chars(dic):
    """
    clean from ['~', '^' ]
    """

    if dic is None: return None
    
    #print(f'dic in fun {dic} ')
    d = {}

    l =['~', '^' ]
    for keys, value in dic.items():
        
        # clean from ['~', '^' ]
        res = [ele for ele in l  if(ele in value)]
        if res:
            d[keys] = value.translate({ord(i): None for i in l })
        else:
            d[keys] = value

        # clean from >= 1.5.0 < 2
    return d

def return_dic_dependencies_out_of_notallowed_chars2(dic):

    if dic is None: return None
    
    #print(f'dic in fun {dic} ')
    d = {}

    for keys, value_version in dic.items():

        list_ver = value_version.split() # split by  ' '

        version_n = [i for i in list_ver if '.' in i] # will get  ceel with '.' char
     
        d[keys] =version_n[0]
 
    #print(f' $$$$ $$$$$$$$')
    return d
            




def start_scraping_npmjs_for_package(search_word, search_keyword_version):
    """
    scrape for keyword
    """
    res = get_page_resource( search_word, search_keyword_version)
    if res == None: return None

    ret_dic = {}

    try:
        dic = res.json()

        #print(f' dic  ### - {dic}')
        # if dic.get() not found is return None
        first_clean_dep=  return_dic_dependencies_out_of_notallowed_chars(dic.get('dependencies'))

        ret_dic['dependencies'] =return_dic_dependencies_out_of_notallowed_chars2(first_clean_dep) # second clean

        ret_dic['number_of_maintainers']= len(dic.get('maintainers'))
        ret_dic['unpackedSize']= dic.get('dist').get('unpackedSize')
        ret_dic['license']= dic.get('license')
        #print(f' \n ^^^^^^^ \n { dic.get("dist").get("unpackedSize")} \n ')
        #print(f' ^^^^ {ret_dic}')
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

    


    

    