from django.shortcuts import render

from packages__app.models import NpmSecurityPackageDeatails
# Create your views here.
from .tasks import build_ml_linear_regression_algorithm
from django.http import JsonResponse
from django.http import HttpResponse
import json
from numpy.random import rand
from rest_framework import views, status
from rest_framework.response import Response
from endpoints.registry import MLRegistry
from packagesAnalyzerProj import create_ml_registry 
from packagesAnalyzerProj.create_ml_registry import registry


from packages__app.models import NpmPackageDependecy,NpmPackage, NpmSecurityPackageDeatails
import joblib # for saving algorithm and preprocessing objects
import numpy as np # for data manipulation
import pandas as pd # for data manipulation
from sklearn.preprocessing import LabelEncoder # for preprocessing

from endpoints.models import Endpoint, MLAlgorithm , MLAlgorithmStatus , MLRequest

# sklearn imports
from sklearn import linear_model
from sklearn import metrics

# helper for logistic regression explanations
from scipy.special import expit
from scipy.special import logit

def task_build_ml_linear_regression_file(request):

    #build()    
    
    build_ml_linear_regression_algorithm.delay()
    return HttpResponse("celery task started  ... ")


def build():
    print(f'    starting task building ML  :-) ')



    #X_data= NpmSecurityPackageDeatails.objects.values_list('number_of_maintainers','unpackedsize').all()
    #Y_data= NpmSecurityPackageDeatails.objects.values_list('is_exploite').all()

    df_X_data = pd.DataFrame(list(NpmSecurityPackageDeatails.objects.values_list('number_of_maintainers','unpackedsize').all()))
    df_Y_data= pd.DataFrame(list(NpmSecurityPackageDeatails.objects.values_list('is_exploite').all()))

    # convert categoricals
    # encoders = {}
    # for column in ['number_of_maintainers', 'unpackedsize', 'license']:
    #     categorical_convert = LabelEncoder()
    #     df_X_data[column] = categorical_convert.fit_transform(df_X_data[column])
    #     encoders[column] = categorical_convert


    lrm=linear_model.LogisticRegression()
    lrm.fit(df_X_data,df_Y_data)

    r_sq = lrm.score(df_X_data,df_Y_data)

    print(f'r_sq : \n  -  {r_sq} -  ')


    print(f' intercept : {lrm.intercept_}')

    print(f' slope : {lrm.coef_}')
    joblib.dump(lrm, "./ML_trained_Data/linear_regression_NpmSecurityPackageDeatails_model.joblib", compress=True)

    print(f' \n finished build_ml_linear_regression_algorithm')

class PredictView(views.APIView):
    def post(self, request, endpoint_name, format=None):

        algorithm_status = self.request.query_params.get("status", "production").strip()
        algorithm_version = self.request.query_params.get("version").strip()

        print(f' looking for - {algorithm_version}')

        algs = MLAlgorithm.objects.filter(parent_endpoint__name = endpoint_name, status__status = algorithm_status, status__active=True)
        #algorithm_version = algorithm_version.strip()

        # for al  in algs:
        #     print(f'al.version-{al.version}-type-{type(al.version)}')
        
        # print(f'algorithm_version-{algorithm_version}-type-{type(algorithm_version)}')
        # counter = 0
        # if algorithm_version is not None:
            
        #     for al in algs:
        #         print(f' len(algorithm_version) {len(algorithm_version)}-  @{algorithm_version}#{al.version}$')
        #         print(f' len(algorithm_version) {len(algorithm_version)}-  @{algorithm_version}#{al.version}$')

        #         if algorithm_version == al.version:
        #             counter = counter +1

            #print(f'algorithm_version-{algorithm_version}-type-{type(al.version)}')
            
            # filter not working 
        #algs = algs.filter(version = algorithm_version)
        #print(f'algs - {algs}')
        if len(algs) == 0:
        #if counter == 0:    
            return Response(
                {"status": "Error", "message": "ML algorithm is not available"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        if len(algs) != 1 and algorithm_status != "ab_testing":
        #if counter!= 1 and algorithm_status != "ab_testing":
            return Response(
                {"status": "Error", "message": "ML algorithm selection is ambiguous. Please specify algorithm version."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        alg_index = 0
        if algorithm_status == "ab_testing":
            alg_index = 0 if rand() < 0.5 else 1

        algorithm_object = registry.endpoints[algs[alg_index].id]

        #algorithm_object = MLRegistry()
        prediction = algorithm_object.compute_prediction(request.data)


        label = prediction["label"] if "label" in prediction else "error"
        ml_request = MLRequest(
            input_data=json.dumps(request.data),
            full_response=prediction,
            response=label,
            feedback="",
            parent_mlalgorithm=algs[alg_index],
        )
        ml_request.save()

        prediction["request_id"] = ml_request.id

        return Response(prediction)
