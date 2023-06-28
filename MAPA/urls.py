from django.urls import path
from MAPA.views import MapagiaListView

urlpatterns = [
    
    path('list_mapa/',MapagiaListView.as_view(),),
    
]