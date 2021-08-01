from django.shortcuts import render

# Create your views here.
from .models import NpmPackage
from django.http import JsonResponse
from django.http import HttpResponse
from .tasks import celery_task_updating_npm_packages_and_dependecies
from django.core import serializers
#from django.forms.models import model_to_dict

def task_view(request):
    celery_task_updating_npm_packages_and_dependecies.delay()
    return HttpResponse("celery task started  ... ")


def package_tree_search(request,search_word, library_name):
    """
        will fetch tree of package from db
    """


    # if package not in db will add package and dependecy recursivlly  - base on old model function  ... need to refine logic
    queryset = NpmPackage()
    queryset.filter_search_npm_package_in_cach_or_db_or_api(search_word)




    queryset = NpmPackage()
        #queryset = NpmPackage.objects.filter(npm_name= search_word)
    #q = queryset.filter_search_npm_package_in_cach_or_db_or_api(search_word)
    #q = NpmPackage.objects.all()
    #dic=  model_to_dict(NpmPackage.objects.all())

    query_exsit = queryset.check_if_package_on_db(search_word)
    print(f' query_exsist: {query_exsit}')
    if not query_exsit:
        return JsonResponse({}, safe=False)

    q = queryset.make_tree_start(search_word)
    #q = serializers.serialize('python', q)
    #print( f'length: {len(q)} ')
    #print(f' \n \n  type:{type(q)}  q: {q} \n \n ')
    #return HttpResponse(q)
    return JsonResponse(q, safe=False)