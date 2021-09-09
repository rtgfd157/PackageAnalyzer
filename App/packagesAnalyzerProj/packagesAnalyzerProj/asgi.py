"""
ASGI config for packagesAnalyzerProj project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'packagesAnalyzerProj.settings')

application = get_asgi_application()


# ML registry
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