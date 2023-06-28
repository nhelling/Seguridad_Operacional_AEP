from django.urls import path
from PINTURA.views import list_pintura,PinturaCreateView,PinturaDeleteView,pintura_update,UpdateView

urlpatterns = [
    path('create_pintura/', PinturaCreateView.as_view(), ),
    path('list_pintura/',list_pintura),
    path('delete_pintura/<int:pk>/',PinturaDeleteView.as_view(), name = 'delete_pintura' ),
    path('update_pintura/<int:pk>/',pintura_update, name = 'pintura_update' ),
    #path('update_pintura/<int:pk>/',UpdateView.as_view(), name = 'pintura_update' ),
]