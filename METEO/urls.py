from django.urls import path
from METEO.views import MeteorologiaListView

urlpatterns = [
    
    path('list_meteorologia/',MeteorologiaListView.as_view(),),
    
]