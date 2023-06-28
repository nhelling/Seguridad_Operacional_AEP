from django.shortcuts import render
from django.views.generic import DeleteView, ListView, CreateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q

from METEO.models import Meteorologia

class MeteorologiaListView(LoginRequiredMixin,ListView):
    model = Meteorologia
    template_name = 'meteorologia/list_meteorologia.html'


