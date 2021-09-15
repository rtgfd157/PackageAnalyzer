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
                                    algorithm_name="linear regression",
                                    algorithm_status="development",
                                    algorithm_version="0.0.1",
                                    owner="idan",
                                    algorithm_description="linear regression with simple pre- and post-processing",
                                    algorithm_code=inspect.getsource(LinearRegressionClassifier))

except Exception as e:
    print("Exception while loading the algorithms to the registry,", str(e))