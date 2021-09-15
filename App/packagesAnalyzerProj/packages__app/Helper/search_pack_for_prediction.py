
from packages__app.Helper.scrape_npmjs import start_scraping_npmjs_for_package, returning_dic_from_pack_security_dic
from django.http import JsonResponse

def search_pack_for_prediction(search_word, search_keyword_version):
    search_keyword_version = search_keyword_version.replace("qqq", ".")

    

    dic1 =   start_scraping_npmjs_for_package(search_word, search_keyword_version )
    # dic2 = returning_dic_from_pack_security_dic(search_word,search_keyword_version)

    if dic1 == None: return JsonResponse({}, safe=False)
    
    ans = {
        'unpackedSize' :   dic1.get('unpackedSize') ,
        'number_of_maintainers' :  dic1.get('number_of_maintainers') 

    }

    return JsonResponse(ans, safe=False)

