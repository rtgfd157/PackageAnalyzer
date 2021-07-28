
from django.shortcuts import render
from rest_framework import viewsets
from .serializers import NpmPackageSerializer, NpmPackageDependecySerializer
from packages__app.models import NpmPackage, NpmPackageDependecy
from rest_framework import generics

from rest_framework import filters # we will use for searching

class NpmPackageView(viewsets.ModelViewSet):
    serializer_class = NpmPackageSerializer
    #queryset = NpmPackage.objects.all()

    search_fields = ['npm_name']
    filter_backends = [filters.SearchFilter]

    def get_queryset(self):
        """
        search for npm package in dependency list for foriegn model keyword
        """
        search_word = self.request.query_params.get('search2')
        print('wwwwwwwwwwwwwwwwww')
        if not ( self.request.method == 'GET' and 'search2' in self.request.GET):
            return NpmPackage.objects.all()
        
        queryset = NpmPackage()
        print('eeeeeeeeeeeeeeeeee')
        #queryset = NpmPackage.objects.filter(npm_name= search_word)
        return queryset.filter_search_npm_package_in_cach_or_db_or_api(search_word)


class NpmPackageDependecyView(viewsets.ModelViewSet):
    serializer_class = NpmPackageDependecySerializer

    search_fields = ['npm_package__npm_name']
    filter_backends = [filters.SearchFilter]

    def get_queryset(self):
        """
        search for npm pacage in dependency list for foriegn model keyword
        """

        

        search_word = self.request.query_params.get('search')

        if not ( self.request.method == 'GET' and 'search' in self.request.GET):
            return NpmPackageDependecy.objects.all()

        queryset = NpmPackageDependecy()
        return queryset.filter_search_npm_package_dep_in_cach_or_db_or_api(search_word)     

        
