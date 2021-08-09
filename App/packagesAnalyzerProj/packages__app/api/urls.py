from django.urls import include, path
from rest_framework.routers import DefaultRouter

from  packages__app.api import views as kv


routerList_packages__app = DefaultRouter()
routerList_packages__app.register(r'npm_package', kv.NpmPackageView, 'npm_package')
routerList_packages__app.register(r'npm_package_dependecy', kv.NpmPackageDependecyView, 'npm_package_dependecy')


urlpatterns = [
        path("count_doc_pacakges_elastic/", 
         kv.ElasticSearchCountDocuments.as_view(),
         name="count-doc-pacakges-elastic"),

         path("count_npm_pacakges_and_dep_packages/", 
         kv.NpmAndNpmDepCounts.as_view(),
         name="count-npm-pacakges-and-dep_packages"),


         
    ]