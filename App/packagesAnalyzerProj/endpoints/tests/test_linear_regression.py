from django.test import TestCase

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