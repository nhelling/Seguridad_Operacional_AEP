from django.urls import path
from PROTOCOLO.views import ProtocoloCreateView,ProtocoloListView,list_protocolo, ProtocoloDeleteView, protocolo_update

urlpatterns = [
    path('create_protocolo/', ProtocoloCreateView.as_view(), ),
    path('list_protocolo/',list_protocolo),
    path('delete_protocolo/<int:pk>/',ProtocoloDeleteView.as_view(), name = 'delete_protocolo' ),
    path('update_protocolo/<int:pk>/',protocolo_update, name = 'protocolo_update' ),
]