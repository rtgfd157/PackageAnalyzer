from django.db import models
from django.test import TestCase
import pprint
from packages__app.Helper import scrape_npmjs 
from packages__app.Helper.search_pack_for_prediction import search_pack_for_prediction
from packages__app.models import NpmPackageDependecy, NpmPackage , NpmSecurityPackageDeatails
from packages__app.Helper.scrape_npmjs import start_scraping_npmjs_for_package
# terminal python3 manage.py test packages__app.tests.test_scraping_npmjs.scraping_Test  --verbosity 2
# python3 manage.py test packages__app.tests.test_search_prediction.search_Predict_Test  --verbosity 2
import urllib.request
# models test
class search_Predict_Test(TestCase):

    def setUp(self):
        
        #np_o= NpmPackage.objects.create(npm_name="test1", version="0.0.1")
        #NpmPackageDependecy.objects.create(npm_package=np_o , npm_package_dep_name="test1_dep", version="0.0.2")

        self.express =search_pack_for_prediction("express", '4.17.1')
        self.should_empty = search_pack_for_prediction("fdrdhjgdrejcfghgf",'11.11.11')
        #self.contents = urllib.request.urlopen("http://127.0.0.1:8000/api/packageSearchForPrediction/express/4qqq17qqq1/").read() 
        
    def test_search_for_prediction(self):

        self.assertEqual(self.express.status_code, 200)
        self.assertEqual(self.express.content, b'{"unpackedSize": 208133, "number_of_maintainers": 3}')
        
        self.assertEqual(self.should_empty.content, b'{}')

        #print(f'self.contents - {self.contents}')
        

        

    






        
        



        