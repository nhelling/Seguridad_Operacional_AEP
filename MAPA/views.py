from django.shortcuts import render
from django.views.generic import DeleteView, ListView, CreateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q

from MAPA.models import Mapa

class MapagiaListView(LoginRequiredMixin,ListView):
    model = Mapa
    template_name = 'mapa/list_mapa.html'
