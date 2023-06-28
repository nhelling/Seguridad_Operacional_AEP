from django.urls import path
from ADR.views import list_adr,AdrCreateView,AdrDeleteView,adr_update

urlpatterns = [

    path('create_adr/', AdrCreateView.as_view(), ),
    path('list_adr/',list_adr),
    path('delete_adr/<int:pk>/',AdrDeleteView.as_view(), name = 'delete_adr' ),
    path('update_adr/<int:pk>/',adr_update, name = 'adr_update' ),

    
]