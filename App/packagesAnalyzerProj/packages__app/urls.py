from django.urls import include, path


from packages__app import views as v


urlpatterns = [

        path("packageTreeSearch/<slug:search_word>/<slug:library_name>/", 
         v.package_tree_search,
         name="comment-create"),
    ]