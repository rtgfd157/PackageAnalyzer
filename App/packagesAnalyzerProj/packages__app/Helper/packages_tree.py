from sys import version
from  packages__app.models import NpmPackage, NpmPackageDependecy, NpmSecurityPackageDeatails
from core.elastic_service import el_search_for_package_tree, upsert_tree_in_el_search
from django.http import JsonResponse
from django.http import HttpResponse
from packages__app.Helper.scrape_npmjs import start_scraping_npmjs_for_package, returning_dic_from_pack_security_dic
from django.shortcuts import get_object_or_404
from django.http import Http404
from packages__app.Helper.tree_build_helper import from_node_to_dic

import threading
lock = threading.Lock()


# function that will return package tree
# made on diff page because, its have lot of code, so i seperate it fro model logic.

# need tp make logic clear
def start_tree(search_word, search_keyword_version):
    #print(f' before search_keyword_version : {search_keyword_version} ')
    search_keyword_version = search_keyword_version.replace("qqq", ".")
    #print(f' search_keyword_version : {search_keyword_version} ')
    
    ans= el_search_for_package_tree(search_word, search_keyword_version)
    #print(f' \n \n \n  from elastic: {ans}  \n \n')

    if len(ans) > 0:
        print(f'return from elastic')
        return JsonResponse(ans, safe=False)

    if not NpmPackage.check_if_package_on_db(search_word, search_keyword_version):
        
        adding_scarp_packages_and_package_dep(search_word, search_keyword_version)
        if not NpmPackage.check_if_package_on_db(search_word, search_keyword_version):
            return JsonResponse({}, safe=False)
        else:
            print(f'query_exsist in db after scrap')
            return found_keyword_on_db_making_tree_upsert_elastic_and_return_front_end(search_word, search_keyword_version)

    else:
        print(f' query_exsist in db ')
        return found_keyword_on_db_making_tree_upsert_elastic_and_return_front_end(search_word, search_keyword_version)
        

        #print(f' q:::::  {q}')
    #q = serializers.serialize('python', q)
    #print( f'length: {len(q)} ')
    #print(f' \n \n  type:{type(q)}  q: {q} \n \n ')
    #return HttpResponse(q)
        
def found_keyword_on_db_making_tree_upsert_elastic_and_return_front_end(search_word, search_keyword_version):
    q = make_tree_start(search_word, search_keyword_version)
    upsert_tree_in_el_search(q)
    return JsonResponse(q, safe=False)

def make_tree_start(search_word, search_keyword_version):
        """
            making recursive tree
            {  npm_name:val , version: val2 , id: val3, dependencies: [  list[0], list[] ]    }

            each node will have the above shape
        """
        
        npm_pack = NpmPackage()

        if not npm_pack.check_if_package_on_db(search_word, search_keyword_version):
            return NpmPackage()
        
        q = populate_tree(search_word, search_keyword_version,[],0)
        return q


def populate_tree( keyword,search_keyword_version ,keyword_search_list =[],loop_number =0):
        """
           node_parent in order to  check  circular call parent->child->parent
           keyword_search_list  - all search word used on branch
        """

        try:
            node = get_object_or_404(NpmPackage, npm_name=keyword , version = search_keyword_version)
        except NpmPackage.DoesNotExist:
            raise Http404("Given NpmPackage query not found....")

        dic = from_node_to_dic(node) # return dictionary from NpmPackage object
        
        npd_query_set =  NpmPackageDependecy.objects.filter(npm_package= node)

        deep_npd_qs= []
        for node_dep in npd_query_set :

            if not ( node_dep.npm_package_dep_name in keyword_search_list): 
                # check for not making cyclic recursion such in "api" npm search  d->es5-ext->es6-iterator->d ....
                keyword_search_list.append( node_dep.npm_package_dep_name )

                # for passing keyword_search_list as value and not refrence [:]
                q = populate_tree(node_dep.npm_package_dep_name, node_dep.version ,keyword_search_list[:], loop_number+1 )
                
                if  q:
                    deep_npd_qs.append(q)
            else:
                print(f' loop number: {loop_number}')
                print(f'  node_dep.npm_package_dep_name  {node_dep.npm_package_dep_name } in keyword list: {len(keyword_search_list)}')
                
        dic['dependencies'] = deep_npd_qs
        return dic




def adding_scarp_packages_and_package_dep( search_word, search_keyword_version):
    """
        will scrap https://registry.npmjs.org/  search_word / search_keyword_version

        and will add both npm package and dependecy package.
        will call filter_search_npm_package_dep_in_cach_or_db_or_api(search_word)

        so, all nesting will be added
    """
    # query npmjs api
    ret_dic = start_scraping_npmjs_for_package(search_word, search_keyword_version)
    #print(f'return dic -{ret_dic} - name: {search_word} ')
    if ret_dic != None:
        npm_pack= NpmPackage(npm_name= search_word , version =  search_keyword_version )
        with lock:
            npm_pack.save()

        nspd_dic = returning_dic_from_pack_security_dic(search_word, search_keyword_version)

        # print(f'@@ {nspd_dic}  -- {type(nspd_dic)} ')

        if  nspd_dic.get('is_exploite') :

            nspd =  NpmSecurityPackageDeatails(npm_package =  npm_pack, number_of_maintainers = ret_dic['number_of_maintainers'],
                    unpackedsize = ret_dic.get('unpackedSize') , license =  ret_dic.get('license') ,
                    is_exploite  =  nspd_dic.get('is_exploite'), num_info_severity =  nspd_dic.get('num_info_severity') ,
                    num_low_severity =  nspd_dic.get('num_low_severity') ,
                     num_moderate_severity =  nspd_dic.get('num_moderate_severity'), num_high_severity = nspd_dic.get('num_high_severity'),
                     num_critical_severity =  nspd_dic.get('num_critical_severity') )
            with lock:
                nspd.save()
        else:
            nspd =  NpmSecurityPackageDeatails(npm_package =  npm_pack, number_of_maintainers = ret_dic['number_of_maintainers'],
                                                is_exploite  =nspd_dic.get('is_exploite'), unpackedsize = ret_dic.get('unpackedSize') )
            with lock:
                nspd.save()  

        ob=  NpmPackageDependecy()
        ob.filter_search_npm_package_dep_in_cach_or_db_or_api(search_word, search_keyword_version,ret_dic['dependencies'])

