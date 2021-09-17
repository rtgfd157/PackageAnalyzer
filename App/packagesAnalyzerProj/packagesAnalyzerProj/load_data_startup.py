

from django.core.management import call_command





from packagesAnalyzerProj.create_ml_registry import LoadMlRegistry
from packages__app.models import NpmPackage
import traceback
from endpoints.models import MLAlgorithm


def start():

    # # loading data on startup  if no data exists
    try:
        query = NpmPackage.objects.all()

        if not query.exists():
            call_command('loaddata', 'data_dump', verbosity=3, database='default')


    except Exception:
        traceback.print_exc()

    try:
    # make ml registry in db  on startup
        clm = LoadMlRegistry()
        clm.create_reg()
    except Exception:
        traceback.print_exc()

    # checking for duplications and removing if occurs
    try:
    
        all_algo =   MLAlgorithm.objects.all()
        for algo in MLAlgorithm.objects.values_list('name','version', flat=False).distinct():
            MLAlgorithm.objects.filter(pk__in=MLAlgorithm.objects.filter(name=algo[0], version=algo[1]).values_list('id', flat=True)[1:]).delete()
    except Exception:
        traceback.print_exc()