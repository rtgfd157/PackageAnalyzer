# backend/server/apps/endpoints/urls.py file
from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from endpoints.api.views import EndpointViewSet
from endpoints.api.views import MLAlgorithmViewSet
from endpoints.api.views import MLAlgorithmStatusViewSet
from endpoints.api.views import MLRequestViewSet


router_list_endpoints = DefaultRouter(trailing_slash=False)
router_list_endpoints.register(r"endpoints", EndpointViewSet, basename="endpoints")
router_list_endpoints.register(r"mlalgorithms", MLAlgorithmViewSet, basename="mlalgorithms")
router_list_endpoints.register(r"mlalgorithmstatuses", MLAlgorithmStatusViewSet, basename="mlalgorithmstatuses")
router_list_endpoints.register(r"mlrequests", MLRequestViewSet, basename="mlrequests")

urlpatterns = [
    url(r"^api/v1/", include(router_list_endpoints.urls)), # not used
]