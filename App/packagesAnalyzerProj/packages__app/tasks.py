from celery import shared_task
import time
from celery.decorators import periodic_task
import datetime as dt
import threading
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import time as t
from celery.utils.log import get_task_logger
from math import ceil
from packages__app.models import NpmPackageDependecy,NpmPackage

from packages__app.Helper.scrape_npmjs import start_scraping_npmjs_for_package

from datetime import datetime, date, time, timedelta

@shared_task
def celery_task_updating_npm_packages_and_dependecies():
    """
        updating Npm packages and their dependecies packages
        will be in the future runing periodically 

        http://127.0.0.1:8000/celery_task_updating_npm_packages_and_dependecies
    """


    print(f'    starting task  :-) ')
    
    now = datetime.now()
    x_time_ago = now - timedelta(days=7)
    outdated_npm_query = NpmPackage.objects.filter(updated_at__lte = x_time_ago)

    for npm_package in outdated_npm_query:
        version_from_scraping = start_scraping_npmjs_for_package(npm_package.npm_name)
        print(f' check : {version_from_scraping}')

        if version_from_scraping != None and ( version_from_scraping  != npm_package.npm_name ):
            npm_package.delete() # delete npm package and npm dependecies (cascading)

            new_npm_package= NpmPackage(npm_name= npm_package.npm_name ,version=version_from_scraping )
            new_npm_package.save() 
            npd =  NpmPackageDependecy()
            npd.filter_search_npm_package_dep_in_cach_or_db_or_api(npm_package.npm_name)


