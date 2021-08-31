
from django.http import response
from django.shortcuts import render
from rest_framework import viewsets
from .serializers import NpmPackageSerializer, NpmPackageDependecySerializer, NpmSecurityPackageDeatailsSerializer
from packages__app.models import NpmPackage, NpmPackageDependecy, NpmSecurityPackageDeatails
from rest_framework import generics

from rest_framework import filters # we will use for searching
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from core.elastic_service import get_packages_tree_count, get_top_most_hits

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


class NpmSecurityPackageDeatailsView(viewsets.ModelViewSet):
    serializer_class = NpmSecurityPackageDeatailsSerializer

    queryset = NpmSecurityPackageDeatails.objects.all().order_by('-is_exploite')
        
class ElasticSearchCountDocuments(APIView):
    """
        a view for counting packages tree in elasticsearch 
    """
    renderer_classes = [JSONRenderer]

    def get(self, request, format=None):
        try:
            documents_counts = get_packages_tree_count()
            print(f'  count: {documents_counts} ')
            c =documents_counts[0]['count']
            content = { c  }
            return Response( content)
        except:
            print('error in class ElasticSearchCountDocuments(APIView):')
            return Response({})

class NpmAndNpmDepCounts(APIView):
    """
        a view for counting packages tree in elasticsearch 
    """
    renderer_classes = [JSONRenderer]

    def get(self, request, format=None):
        try:
            npm = NpmPackage.objects.all().count()
            npm_dep = NpmPackageDependecy.objects.all().count()
            #print(f'  count: {documents_counts} ')
            
            content = { 'npm_count': npm, 
                        'npm_dep_count': npm_dep
             }
            return Response( content)
        except:
            print('error in class NpmAndNpmDepCounts(APIView):')
            return Response({})


class TopPackagesElastic(APIView):
    """
        return topm most hits of packages
    """

    def get(self, request, format=None):
        try:

            doc_top_hits = get_top_most_hits()

            #print(f' doc_top_hits: { doc_top_hits}  ')
            return Response( doc_top_hits)
        except:
            print('error in class TopPackagesElastic(APIView):')
            return Response({})

