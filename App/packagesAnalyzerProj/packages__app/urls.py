from django.urls import include, path


from packages__app import views as v


urlpatterns = [

        path("packageTreeSearch/<slug:search_keyword_npm_pack>/<slug:search_keyword_version>/", 
         v.package_tree_search,
         name="search"),

         path("packageSearchForPrediction/<slug:search_keyword_npm_pack>/<slug:search_keyword_version>/", 
         v.package_prediction_search,
         name="search-for-prediction"),


         path("test_see_diff_between_npm_to_security/", 
         v.test_see_diff_between_npm_to_security,
         name="test_see_diff_between_npm_to_security"),


         
    ]