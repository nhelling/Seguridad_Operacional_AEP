from django.urls import path

from DERRAMES.views import DerrameCreateView,DerrameListView,list_derrame, DerrameDeleteView, derrame_update

urlpatterns = [
    path('create_derrame/', DerrameCreateView.as_view(), ),
    path('list_derrame/',list_derrame),
    path('delete_derrame/<int:pk>/',DerrameDeleteView.as_view(), name = 'delete_derrame' ),
    path('update_derrame/<int:pk>/',derrame_update, name = 'derrame_update' ),
]