from django.urls import path
from VIENTO.views import VientologiaListView

urlpatterns = [
    
    path('list_viento/',VientologiaListView.as_view(),),
    
]