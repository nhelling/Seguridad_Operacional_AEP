from django.urls import path
from initial.views import list_initial

urlpatterns = [
    path('index/', list_initial),
    
]