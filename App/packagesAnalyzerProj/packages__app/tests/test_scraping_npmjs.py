from django.db import models
from django.test import TestCase

from packages__app.Helper import scrape_npmjs 
from packages__app.models import NpmPackageDependecy, NpmPackage

# terminal python3 manage.py test packages__app.tests.test_scraping_npmjs.scraping_Test  --verbosity 2

# models test
class scraping_Test(TestCase):

    def setUp(self):
        
        #np_o= NpmPackage.objects.create(npm_name="test1", version="0.0.1")
        #NpmPackageDependecy.objects.create(npm_package=np_o , npm_package_dep_name="test1_dep", version="0.0.2")

        self.express =scrape_npmjs.start_scraping_npmjs_for_package("express")
        self.should_empty =scrape_npmjs.start_scraping_npmjs_for_package("fdrdhjgdrejcfghgf")
        
        
    def test_number_of_value_list_vs_object_queryset(self):

        #test page not reached  not added
        # r =scrape_npmjs.start_scraping_npmjs_for_word("fjfghfhgfstrhghyth")

        self.assertEqual(None,  self.should_empty )

        # test added 
        #print(f'self.express:{self.express} ')

        # l = NpmPackage.objects.all()  
        # print(f' \n l:{l}  \n')
        # self.assertTrue( len(l)>0 )

        # print(f'\n \n ggg - {l} ')
        # l = NpmPackageDependecy.objects.all()
        # self.assertTrue( len(l)>0 )
        self.assertTrue(self.express)

    def test_npm_registry_fetch_for_package_security(self):

        # known vulnarabilty in version
        stdout, stderr =scrape_npmjs.start_npm_registry_fetch_for_package_security("express", '0.21.1')
        #stdout, stderr =scrape_npmjs.start_npm_registry_fetch_for_package_security("vue", '2.6.14')
        #stdout, stderr =scrape_npmjs.start_npm_registry_fetch_for_package_security("axios", '0.21.1')
        #print(  '------stdout------',stdout['actions'])
        #print(  '-------stderr-----',stderr)
        #print('--stdout-- ' , stdout)
        self.assertTrue(len(stdout['actions']) > 0)
        #self.assertTrue(stderr == None)

        #print(' $$$$$$$$$$$$ ',type(stdout))
        
        # import pprint
        # pprint.pprint(stdout['metadata'] ['vulnerabilities']['low']) # ['actions']
        #print(f' {stdout.decode("utf8")}  \n \n  ')

        # stdout, stderr  =scrape_npmjs.start_npm_registry_fetch_for_package_security("fdrdhjgdrejcfghgf", '11.11.11')
        # self.assertTrue(stdout['actions'] == [])

        #print(  '-------stdout-----',stdout)
        # print(  '------------',stdout['actions'])
        
        #self.assertTrue(len(stderr) > 0)
        # self.assertTrue(len(stderr) == 0)
        # self.assertTrue(len(stderr) > 0)
        # self.assertTrue(len(stdout) == 0)

    def test_returning_dic_from_pack_security_dic(self):

        val  = scrape_npmjs.returning_dic_from_pack_security_dic("vue", '2.6.14')

        #print( f'val - {val}')
        self.assertFalse( val['is_exploite']  )




        