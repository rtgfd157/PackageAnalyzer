from celery import shared_task
import time
from celery.decorators import periodic_task
import datetime as dt
import threading
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import time as t
from celery.utils.log import get_task_logger
from math import ceil
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

from datetime import datetime, date, time, timedelta

@shared_task
def build_ml_linear_regression_algorithm():
    """
        X:
            build file that will posses linear regression algorithm for decideing if packages is exploite based on fields:
            number_of_maintainers - of npm_package
            unpackedsize - size of the package
            license - kind of license of the package e.g -(MIT ...)
            num_high_severity - npm audit number of  high severity bugs in program 
            num_moderate_severity - npm audit number of  moderate severity bugs in program
            num_low_severity - npm audit number of  low severity bugs in program
            num_critical_severity - npm audit number of  critical severity bugs in program
            num_info_severity - ...


        Y:
            is_exploite - if npm audit find the package have exploite


        http://127.0.0.1:8000/celery_task_build_ml_linear_regression_file
    """


    print(f'    starting task building ML  :-) ')



    X_data= NpmSecurityPackageDeatails.objects.values_list('number_of_maintainers','unpackedsize','license').all()
    Y_data= NpmSecurityPackageDeatails.objects.values_list('is_exploite').all()

    df_X_data = pd.DataFrame(list(NpmSecurityPackageDeatails.objects.values_list('number_of_maintainers','unpackedsize','license').all()))
    df_Y_data= pd.DataFrame(list(NpmSecurityPackageDeatails.objects.values_list('is_exploite').all()))

    # convert categoricals
    encoders = {}
    for column in ['number_of_maintainers', 'unpackedsize', 'license']:
        categorical_convert = LabelEncoder()
        df_X_data[column] = categorical_convert.fit_transform(df_X_data[column])
        encoders[column] = categorical_convert


    lrm=linear_model.LogisticRegression()
    lrm.fit(df_X_data,df_Y_data)

    joblib.dump(lrm, "./linear_regression_NpmSecurityPackageDeatails_model.joblib", compress=True)

    print(f' \n finished build_ml_linear_regression_algorithm')

    #print(f'd  - {d}')
    
