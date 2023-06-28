from django.urls import path
from BSO.views import list_bso,BsoCreateView,BsoDeleteView,bso_update

urlpatterns = [

    path('create_bso/', BsoCreateView.as_view(), ),
    path('list_bso/',list_bso),
    path('delete_bso/<int:pk>/',BsoDeleteView.as_view(), name = 'delete_bso' ),
    path('update_bso/<int:pk>/',bso_update, name = 'bso_update' ),

    
]