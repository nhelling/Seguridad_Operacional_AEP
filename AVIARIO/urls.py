from django.urls import path

from AVIARIO.views import AviarioCreateView,AviarioListView,list_aviario, AviarioDeleteView, aviario_update

urlpatterns = [
    path('create_aviario/', AviarioCreateView.as_view(), ),
    path('list_aviario/',list_aviario),
    path('delete_aviario/<int:pk>/',AviarioDeleteView.as_view(), name = 'delete_aviario' ),
    path('update_aviario/<int:pk>/',aviario_update, name = 'aviario_update' ),
]