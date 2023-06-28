from django.shortcuts import render
from django.views.generic import DeleteView, ListView, CreateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q

from VIENTO.models import Viento

class VientologiaListView(LoginRequiredMixin,ListView):
    model = Viento
    template_name = 'viento/list_viento.html'
