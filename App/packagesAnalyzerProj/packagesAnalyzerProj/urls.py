"""packagesAnalyzerProj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework.routers import DefaultRouter,SimpleRouter
from django.conf import settings
from packages__app.api.urls import routerList_packages__app
from endpoints.api.urls import router_list_endpoints

from packages__app import views as views_packages__app
from endpoints import views as views_endpoints


router = DefaultRouter()
router.registry.extend(routerList_packages__app.registry)
router.registry.extend(router_list_endpoints.registry)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path("api/",include("packages__app.api.urls")),
    path("api/",include("packages__app.urls")),
    path('celery_task_updating_npm_packages_and_dependecies', views_packages__app.task_view ),
    path('celery_task_build_ml_linear_regression_file', views_endpoints.task_build_ml_linear_regression_file ),


]


# current solution put it here for 1 call in startup

import inspect
from endpoints.registry import MLRegistry
from endpoints.ml.linear_regression_NpmSecurity_Classifier import LinearRegressionClassifier

try:
            registry = MLRegistry() # create ML registry
            # Random Forest classifier
            rf = LinearRegressionClassifier()
            # add to ML registry
            registry.add_algorithm(endpoint_name="linear_regression_classifier",
                                    algorithm_object=rf,
                                    algorithm_name="random forest",
                                    algorithm_status="production",
                                    algorithm_version="0.0.1",
                                    owner="idan",
                                    algorithm_description="linear regression with simple pre- and post-processing",
                                    algorithm_code=inspect.getsource(LinearRegressionClassifier))

except Exception as e:
    print("Exception while loading the algorithms to the registry,", str(e))

   