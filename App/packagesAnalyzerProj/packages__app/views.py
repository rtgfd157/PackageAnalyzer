from django.shortcuts import render

# Create your views here.
from .models import NpmPackage, NpmSecurityPackageDeatails , NpmPackageDependecy
from django.http import JsonResponse
from django.http import HttpResponse
from .tasks import celery_task_updating_npm_packages_and_dependecies
from django.core import serializers
from core.elastic_service import el_search_for_package_tree, upsert_tree_in_el_search
from packages__app.Helper.packages_tree import start_tree
#from django.forms.models import model_to_dict

def task_view(request):
    celery_task_updating_npm_packages_and_dependecies.delay()
    return HttpResponse("celery task started  ... ")


def package_tree_search(request,search_keyword_npm_pack, search_keyword_version):
    """
        will fetch tree of package from db
    """
    return start_tree(search_keyword_npm_pack, search_keyword_version)

def test_see_diff_between_npm_to_security(self):
        npm_sec= NpmSecurityPackageDeatails.objects.all()
        npm_packages = NpmPackage.objects.all()

        #print(f' !!!!!!!!!!!!{npm_sec}!!!!!!!!!!!!!!!!')

        for pack in npm_packages:
            #print(pack)
            is_in_both = npm_sec.filter( npm_package__id = pack.id )
            #print( is_in_both )
            if not is_in_both.exists():
                print(f'\n ----{pack}---- \n')
            # else:
            #     print('  ^^^^')

        return HttpResponse('backkk')

