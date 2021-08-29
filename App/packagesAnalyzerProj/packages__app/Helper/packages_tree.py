from  packages__app.models import NpmPackage, NpmPackageDependecy
from core.elastic_service import el_search_for_package_tree, upsert_tree_in_el_search
from django.http import JsonResponse
from django.http import HttpResponse
from packages__app.Helper.scrape_npmjs import start_scraping_npmjs_for_package_dependencies, start_scraping_npmjs_for_package
from django.shortcuts import get_object_or_404
from django.http import Http404
from packages__app.Helper.tree_build_helper import from_node_to_dic

import threading
lock = threading.Lock()


# function that will return package tree
# made on diff page because, its have lot of code, so i seperate it fro model logic.


def start_tree(search_word, library_name):
    
    str_report = ''
    
    ans= el_search_for_package_tree(search_word)
    #print(f' \n \n \n  from elastic: {ans}  \n \n')

    if len(ans) > 0:
        print(f'return from elastic')
        return JsonResponse(ans, safe=False)

    # if package not in db will add package and dependecy recursivlly  - base on old model function  ... need to refine logic
    filter_search_npm_package_in_cach_or_db_or_api(search_word)


    queryset = NpmPackage()


    query_exists = queryset.check_if_package_on_db(search_word)
    print(f' query_exsist: {query_exists}')
    if not query_exists:
        print(f'return from db')
        return JsonResponse({}, safe=False)
    else:

        q = make_tree_start(search_word)
        print(f'return from api')
        #print(f' q:::::  {q}')
        upsert_tree_in_el_search(q)
    #q = serializers.serialize('python', q)
    #print( f'length: {len(q)} ')
    #print(f' \n \n  type:{type(q)}  q: {q} \n \n ')
    #return HttpResponse(q)
    return JsonResponse(q, safe=False)



def make_tree_start(search_word):
        """
            making recursive tree
            {  npm_name:val , version: val2 , id: val3, dependencies: [  list[0], list[] ]    }

            each node will have the above shape
        """
        
        npm_pack = NpmPackage()

        if not npm_pack.check_if_package_on_db(search_word):
            return NpmPackage()
        
        q = populate_tree(search_word,[],0)
        return q

def filter_search_npm_package_in_cach_or_db_or_api(search_word):
        """
            search the word in db if not, in api request to npmjs.com
            need to implement caching in elasticsearch
        """

        # query our db
        queryset = NpmPackage.objects.filter(npm_name=search_word)
        if  queryset.exists():
            return queryset 
        
        else:

            NpmPackage.adding_scarp_packages_and_package_dep(search_word)
            return NpmPackage.objects.filter(npm_name=search_word)

def populate_tree( keyword, keyword_search_list =[],loop_number =0):
        """
           node_parent in order to  check  circular call parent->child->parent
           keyword_search_list  - all search word used on branch
        """

        try:
            node = get_object_or_404(NpmPackage, npm_name=keyword)
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
                q = populate_tree(node_dep.npm_package_dep_name, keyword_search_list[:], loop_number+1 )
                
                if  q:
                    deep_npd_qs.append(q)
            else:
                print(f' loop number: {loop_number}')
                print(f'  node_dep.npm_package_dep_name  {node_dep.npm_package_dep_name } in keyword list: {len(keyword_search_list)}')
                
        dic['dependencies'] = deep_npd_qs
        return dic







