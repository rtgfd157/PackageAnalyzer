from django.urls import include, path


from endpoints.views import PredictView # import PredictView


urlpatterns = [


    path("predict/<slug:endpoint_name>/", 
         PredictView.as_view(),
         name="predict"),

  


         
    ]