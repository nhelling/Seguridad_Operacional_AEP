from django.urls import path
from CAPACITACION.views import list_capacitacion,CapacitacionCreateView,CapacitacionDeleteView,capacitacion_update

urlpatterns = [

    path('create_capacitacion/', CapacitacionCreateView.as_view(), ),
    path('list_capacitacion/',list_capacitacion),
    path('delete_capacitacion/<int:pk>/',CapacitacionDeleteView.as_view(), name = 'capacitacion_bso' ),
    path('update_capacitacion/<int:pk>/',capacitacion_update, name = 'capacitacion_update' ),

    
]