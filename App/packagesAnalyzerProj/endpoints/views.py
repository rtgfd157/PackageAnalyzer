from django.shortcuts import render

from packages__app.models import NpmSecurityPackageDeatails
# Create your views here.
from .tasks import build_ml_linear_regression_algorithm
from django.http import JsonResponse
from django.http import HttpResponse


from packages__app.models import NpmPackageDependecy,NpmPackage, NpmSecurityPackageDeatails
import joblib # for saving algorithm and preprocessing objects
import numpy as np # for data manipulation
import pandas as pd # for data manipulation
from sklearn.preprocessing import LabelEncoder # for preprocessing

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
    joblib.dump(lrm, "./linear_regression_NpmSecurityPackageDeatails_model.joblib", compress=True)

    print(f' \n finished build_ml_linear_regression_algorithm')