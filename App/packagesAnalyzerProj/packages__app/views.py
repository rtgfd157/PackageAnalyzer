from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse
from .tasks import celery_task_updating_npm_packages_and_dependecies

def task_view(request):
    celery_task_updating_npm_packages_and_dependecies.delay()
    return HttpResponse("celery task started  ... ")