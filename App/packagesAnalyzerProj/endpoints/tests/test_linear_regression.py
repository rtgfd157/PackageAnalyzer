from django.test import TestCase
import inspect
from endpoints.registry import MLRegistry
from endpoints.ml.linear_regression_NpmSecurity_Classifier import LinearRegressionClassifier

# python3 manage.py test endpoints.tests.test_linear_regression.MLTests  --verbosity 2

class MLTests(TestCase):
    def test_lr_algorithm(self):
        input_data = {
            "number_of_maintainers": 6,
            "unpackedsize": 1634521
        }

        my_alg = LinearRegressionClassifier()
        response = my_alg.compute_prediction(input_data)
        print(f' responses - {response}')
        self.assertEqual('OK', response['status'])
        self.assertTrue('label' in response)
        self.assertEqual('<=50K', response['label'])


    def test_lr_algorithm2(self):
        input_data = {
            "number_of_maintainers": 1,
            "unpackedsize": 1024
        }

        my_alg = LinearRegressionClassifier()
        response = my_alg.compute_prediction(input_data)
        print(f' responses - {response}')
        self.assertEqual('OK', response['status'])
        self.assertTrue('label' in response)
        self.assertEqual('<=50K', response['label'])

    # add below method to MLTests class:
    def test_registry(self):
        registry = MLRegistry()
        self.assertEqual(len(registry.endpoints), 0)
        endpoint_name = "income_classifier"
        algorithm_object = LinearRegressionClassifier()
        algorithm_name = "linear regression"
        algorithm_status = "production"
        algorithm_version = "0.0.1"
        algorithm_owner = "idan"
        algorithm_description = "linear regression with simple pre- and post-processing"
        algorithm_code = inspect.getsource(LinearRegressionClassifier)
        # add to registry
        registry.add_algorithm(endpoint_name, algorithm_object, algorithm_name,
                    algorithm_status, algorithm_version, algorithm_owner,
                    algorithm_description, algorithm_code)
        # there should be one endpoint available
        self.assertEqual(len(registry.endpoints), 1)