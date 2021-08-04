from django.db import models
from django.db.models.fields.mixins import NOT_PROVIDED
from django.db.models.query_utils import Q
from packages__app.Helper.scrape_npmjs import start_scraping_npmjs_for_package_dependencies, start_scraping_npmjs_for_package
from django.shortcuts import get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from itertools import chain
from django.core import serializers
from django.shortcuts import get_object_or_404
from django.http import Http404

class NpmPackage(models.Model):
    """
        npm package info
    """

    npm_name = models.CharField(max_length=100)
    version = models.CharField(max_length=16)
    updated_at = models.DateField( auto_now=True)

    def __str__(self):
        return self.npm_name 

    def filter_search_npm_package_in_cach_or_db_or_api(self, search_word):
        """
            search the word in db if not, in api request to npmjs.com
            need to implement caching in elasticsearch
        """

        # query our db
        queryset = NpmPackage.objects.filter(npm_name=search_word)
        if  queryset.exists():
            return queryset 
        
        else:
            self.adding_scarp_packages_and_package_dep(search_word)
            return NpmPackage.objects.filter(npm_name=search_word)


    def adding_scarp_packages_and_package_dep(self, search_word):
        """
            will scrap https://registry.npmjs.org/  var   /latest

            and will add both npm package and dependecy package.
            will call filter_search_npm_package_dep_in_cach_or_db_or_api(search_word)

            so, all nesting will be added
        """
        # query npmjs api
        version = start_scraping_npmjs_for_package(search_word)
        print(f'version-{version} ')
        if version != None:
            queryset= NpmPackage(npm_name= search_word ,version=version )
            queryset.save() 
            ob=  NpmPackageDependecy()
            ob.filter_search_npm_package_dep_in_cach_or_db_or_api(search_word)

    def check_if_package_on_db(self,search_word):
        queryset = NpmPackage.objects.filter(npm_name=search_word)
        if  queryset.exists():
            return True
        return False

    def make_tree_start(self,search_word):
        """
            making recursive tree
            {  npm_name:val , version: val2 , id: val3, dependencies: [  list[0], list[] ]    }

            each node will have the above shape
        """

        if not self.check_if_package_on_db(search_word):
            return NpmPackage()
        
        q = self.populate_tree(search_word)
        return q

    def populate_tree(self, keyword, keyword_search_list =[]):
        """
           node_parent in order to  check  circular call parent->child->parent
           keyword_search_list  - all search word used on branch
        """

        dic = {}
        try:
            node = get_object_or_404(NpmPackage, npm_name=keyword)
        except NpmPackage.DoesNotExist:
            raise Http404("Given NpmPackage query not found....")
        #node = NpmPackage.objects.filter(npm_name=keyword)
        dic['npm_name'] = node.npm_name
        dic['version'] = node.version
        dic['id'] = node.id

        dic['dependencies'] ={}

        npd_query_set =  NpmPackageDependecy.objects.filter(npm_package= node)

        deep_npd_qs= []
        for node_dep in npd_query_set :

            if not node_dep.npm_package_dep_name in keyword_search_list: 
                # check for not making cyclic recursion such in "api" npm search  d->es5-ext->es6-iterator->d ....
                keyword_search_list.append( node.npm_name )
                q = self.populate_tree(node_dep.npm_package_dep_name, keyword_search_list )
                if  q:
                    deep_npd_qs.append(q)
                    dic['dependencies'].update( q  )
                    #dic['dependencies'] |= q
                    #npd_query_set |= q
                
        dic['dependencies'] = deep_npd_qs

        return dic


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

    def filter_search_npm_package_dep_in_cach_or_db_or_api(self, search_word):
        """
            search the word in db if not, in api request to npmjs.com
            need to implement caching in elasticsearch
        """

        # query our db
        queryset = NpmPackageDependecy.objects.filter(npm_package__npm_name=search_word)
        if  queryset.exists():
            print("exsist ")
            return queryset 
        
        else:
            # query npmjs api
            dependecies = start_scraping_npmjs_for_package_dependencies(search_word)
            # print(f'dependecies-{dependecies} ')
            if dependecies != None:
                self.insert_package_dependecy_bulk_from_scraping(dependecies, search_word)

            return NpmPackageDependecy.objects.filter(npm_package__npm_name=search_word)

    def insert_package_dependecy_bulk_from_scraping(self,  dependecies, search_word):

        package_object = get_object_or_404(NpmPackage, npm_name=search_word)
        dep_list = []
        for name, version in dependecies.items():
            # name -key , version - value
            npd =  NpmPackageDependecy(npm_package = package_object, npm_package_dep_name=name, version= version)
            dep_list.append( npd )
        NpmPackageDependecy.objects.bulk_create(dep_list)

        for name, version in dependecies.items():
            self.add_if_dep_package_not_in_npmPackage_model(name)

    def add_if_dep_package_not_in_npmPackage_model(self, search_word):
        """
            will add dependecy package also in npmPackage model if not exists 
        """
        try:
            ob  = NpmPackage.objects.get(npm_name=search_word)
        except ObjectDoesNotExist:
            ob = NpmPackage()
            ob.adding_scarp_packages_and_package_dep(search_word)
