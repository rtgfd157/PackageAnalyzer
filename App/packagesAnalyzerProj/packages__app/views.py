from django.shortcuts import render

# Create your views here.
from .models import NpmPackage
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


def package_tree_search(request,search_word, library_name):
    """
        will fetch tree of package from db
    """
    return start_tree(search_word, library_name)