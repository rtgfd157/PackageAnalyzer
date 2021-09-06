from django.db import models
from django.db.models.fields.mixins import NOT_PROVIDED
from django.db.models.query_utils import Q
from packages__app.Helper.scrape_npmjs import  start_scraping_npmjs_for_package
from django.shortcuts import get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from itertools import chain
from django.core import serializers
from django.http import Http404
from packages__app.Helper.threading_helper import start_threading_scrap_insert
import threading
from django.shortcuts import get_list_or_404, get_object_or_404

lock = threading.Lock()

class NpmPackage(models.Model):
    """
        npm package info
    """

    npm_name = models.CharField(max_length=100)
    version = models.CharField(max_length=16)
    updated_at = models.DateField( auto_now=True)

    def __str__(self):
        return self.npm_name 

    @staticmethod
    def check_if_package_on_db(search_word, search_keyword_version):
        queryset = NpmPackage.objects.filter(npm_name=search_word, version = search_keyword_version )
        if  queryset.exists():
            return True
        return False

    
    

    

    


class NpmPackageDependecy(models.Model):
    """
        model will show library that NpmPackage depend upon
    """

    npm_package = models.ForeignKey(NpmPackage, on_delete=models.CASCADE)
    npm_package_dep_name = models.CharField(max_length=100)
    version = models.CharField(max_length=16)
    updated_at =  models.DateField( auto_now=True)

    def __str__(self):
        return self.npm_package_dep_name + " " + self.version

    def filter_search_npm_package_dep_in_cach_or_db_or_api(self, search_word, search_keyword_version , dependencies):
        """
            search the word in db if not, in api request to npmjs.com 
        """
        
        
        # query our db
        queryset = NpmPackageDependecy.objects.filter(npm_package__npm_name=search_word, npm_package__version = search_keyword_version)
        if  queryset.exists():
            return queryset 
        
        else:
            # query npmjs api
            
            # print(f'dependecies-{dependecies} ')
            if dependencies != None:
                # will act as start and ending point for other threads
                #start_end_threading_point(self.insert_package_dependecy_bulk_from_scraping , dependecies, search_word )
                self.insert_package_dependecy_bulk_from_scraping(dependencies, search_word , search_keyword_version)
                 
            return NpmPackageDependecy.objects.filter(npm_package__npm_name=search_word)

    def insert_package_dependecy_bulk_from_scraping(self,  dependecies, search_word, search_keyword_version):

        package_object = get_object_or_404(NpmPackage, npm_name=search_word , version = search_keyword_version)
        dep_list = []
        for name, version in dependecies.items():
            # name -key , version - value
            npd =  NpmPackageDependecy(npm_package = package_object, npm_package_dep_name=name, version= version)
            dep_list.append( npd )

        with lock:    
            NpmPackageDependecy.objects.bulk_create(dep_list)
        
        is_threaded =False

        if is_threaded:
            start_threading_scrap_insert(len(dependecies), dependecies, self.add_if_dep_package_not_in_npmPackage_model )
            
        else:
            for name, version in dependecies.items():
                self.add_if_dep_package_not_in_npmPackage_model(name, version ,search_keyword_version)

    def add_if_dep_package_not_in_npmPackage_model(self, npm_name, version ,search_keyword_version):
        """
            will add dependecy package also in npmPackage model if not exists 
        """
        try:
            ob  = NpmPackage.objects.get(npm_name=npm_name, version = search_keyword_version)
        except ObjectDoesNotExist:
            from packages__app.Helper.packages_tree import adding_scarp_packages_and_package_dep as ad
            ad(npm_name, version)



class NpmSecurityPackageDeatails(models.Model):
    '''
        this will act as data that will hold fields for ML algo

        Attributes:
        npm_package - NpmPackage model FK
        number_of_maintainers - of npm_package
        unpackedsize - size of the package
        license - kind of license of the package e.g -(MIT ...)
        is_exploite - if npm audit find the package have exploite
        num_high_severity - npm audit number of  high severity bugs in program 
        num_moderate_severity - npm audit number of  moderate severity bugs in program
        num_low_severity - npm audit number of  low severity bugs in program
        num_critical_severity - npm audit number of  critical severity bugs in program
        num_info_severity - ...
    '''

    npm_package = models.ForeignKey(NpmPackage, on_delete=models.CASCADE)
    number_of_maintainers = models.IntegerField(default = 1 , null =True)
    unpackedsize = models.IntegerField(null =True) # IntegerField - can hold up to 268 MB
    license = models.CharField(max_length=36, null=True, blank=True )
    updated_at = models.DateField( auto_now=True)
    is_exploite = models.BooleanField()
    num_high_severity = models.IntegerField(default = 0 , null =True, blank =True)
    num_moderate_severity = models.IntegerField(default = 0 , null =True, blank =True)
    num_low_severity = models.IntegerField(default = 0 , null =True, blank =True)
    num_info_severity = models.IntegerField(default = 0 , null =True, blank =True)
    num_critical_severity = models.IntegerField(default = 0 , null =True, blank =True)

    def __str__(self):
        return   " security package model: " + self.npm_package.npm_name +' is exploite: '+ str(self.is_exploite)

    def return_version_npm(self):
        return self.npm_package.version


class NpmProblemCallApi(models.Model):
    """
        npm package info of pacakages that couldnt been harvest
    """

    npm_package_name_problem = models.CharField(max_length=100)
    version_problem = models.CharField(max_length=16)
    updated_at = models.DateField( auto_now=True)


    def __str__(self):
        return   " security package model: " + self.npm_package_name_problem+' version: '+ self.version_problem 

