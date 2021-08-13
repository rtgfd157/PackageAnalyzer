from  packages__app.models import NpmPackage, NpmPackageDependecy
from core.elastic_service import el_search_for_package_tree, upsert_tree_in_el_search
from django.http import JsonResponse
from django.http import HttpResponse


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
    queryset = NpmPackage()
    queryset.filter_search_npm_package_in_cach_or_db_or_api(search_word)


    queryset = NpmPackage()


    query_exists = queryset.check_if_package_on_db(search_word)
    print(f' query_exsist: {query_exists}')
    if not query_exists:
        print(f'return from db')
        return JsonResponse({}, safe=False)
    else:

        q = queryset.make_tree_start(search_word)
        print(f'return from api')
        #print(f' q:::::  {q}')
        upsert_tree_in_el_search(q)
    #q = serializers.serialize('python', q)
    #print( f'length: {len(q)} ')
    #print(f' \n \n  type:{type(q)}  q: {q} \n \n ')
    #return HttpResponse(q)
    return JsonResponse(q, safe=False) 

