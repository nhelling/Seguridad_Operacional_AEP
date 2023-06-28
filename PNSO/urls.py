from django.urls import path
from PNSO.views import PnsoCreateView,PnsoListView,list_pnso, PnsoDeleteView, pnso_update

urlpatterns = [
    path('create_pnso/', PnsoCreateView.as_view(), ),
    path('list_pnso/',list_pnso),
    path('delete_pnso/<int:pk>/',PnsoDeleteView.as_view(), name = 'delete_pnso' ),
    path('update_pnso/<int:pk>/',pnso_update, name = 'pnso_update' ),
]