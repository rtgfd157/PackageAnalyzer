from django.urls import include, path
from rest_framework.routers import DefaultRouter

from  packages__app.api import views as kv


routerList_packages__app = DefaultRouter()
routerList_packages__app.register(r'npm_package', kv.NpmPackageView, 'npm_package')
routerList_packages__app.register(r'npm_package_dependecy', kv.NpmPackageDependecyView, 'npm_package_dependecy')


urlpatterns = [


    ]