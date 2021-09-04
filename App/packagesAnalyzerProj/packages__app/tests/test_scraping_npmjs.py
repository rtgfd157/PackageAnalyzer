from django.db import models
from django.test import TestCase
import pprint
from packages__app.Helper import scrape_npmjs 
from packages__app.Helper import packages_tree
from packages__app.models import NpmPackageDependecy, NpmPackage , NpmSecurityPackageDeatails

# terminal python3 manage.py test packages__app.tests.test_scraping_npmjs.scraping_Test  --verbosity 2

# models test
class scraping_Test(TestCase):

    def setUp(self):
        
        #np_o= NpmPackage.objects.create(npm_name="test1", version="0.0.1")
        #NpmPackageDependecy.objects.create(npm_package=np_o , npm_package_dep_name="test1_dep", version="0.0.2")

        self.express =scrape_npmjs.start_scraping_npmjs_for_package("express", '4.17.1')
        self.should_empty =scrape_npmjs.start_scraping_npmjs_for_package("fdrdhjgdrejcfghgf",'11.11.11')
        
        
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

        


    # def test_see_diff_between_npm_to_security(self):
    #     ret = scrape_npmjs.start_npm_registry_fetch_for_package_security('vue','2.6.14')

    #     pprint.pprint(f'\n  1) ret  {ret}\n    ')

    #     ret = scrape_npmjs.returning_dic_from_pack_security_dic('vue','2.6.14')

    #     pprint.pprint(f'\n 2) ret  {ret}\n    ')


    def test_is_exploite_npm_security(self):
        packages_tree.adding_scarp_packages_and_package_dep("marked", '0.6.3')

        # known to have security problems

        a = NpmSecurityPackageDeatails.objects.get(npm_package__npm_name ="marked" , npm_package__version = '0.6.3')


        self.assertTrue(a.is_exploite)

    def test_if_dependecy_name_ok(self):
        l =['~', '^' , '>' , '=' , '>' , ' ' ]

        res = scrape_npmjs.get_page_resource( 'express', '4.15.0')
        dic = res.json()
        d = scrape_npmjs.return_dic_dependencies_out_of_notallowed_chars(dic.get('dependencies'))

        bol =False

        for c in l:
            if c in d.values():
                bol= True
        self.assertFalse(bol)


    def test_chars_in_version(self):
        # known to have     "statuses": ">= 1.5.0 < 2",
        l =['~', '^' , '>' , '=' , '>' , ' ' ]

        res = scrape_npmjs.get_page_resource( 'http-errors', '1.7.2')
        dic = res.json()

        # will clean from ~ ^
        first_clean_dep = scrape_npmjs.return_dic_dependencies_out_of_notallowed_chars(dic.get('dependencies'))

        # will clean from >= 1.5.0 < 2
        d= scrape_npmjs.return_dic_dependencies_out_of_notallowed_chars2(first_clean_dep) 
        print(f'\n {d}')

        bol =False

        for c in l:
            if c in d.values():
                bol= True
        self.assertFalse(bol)
        



        