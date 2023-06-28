from django.shortcuts import render
from django.views.generic import DeleteView, ListView, CreateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q

from DERRAMES.models import Derrame
from DERRAMES.forms import DerrameForm

class DerrameCreateView(LoginRequiredMixin,CreateView):
    model = Derrame
    template_name = 'derrame/create_derrame_full.html'
    fields = '__all__'
    success_url = '/DERRAMES/list_derrame/'

class DerrameListView(LoginRequiredMixin,ListView):
    model = Derrame
    template_name = 'derrame/list_derrame.html'

@login_required 
def list_derrame(request):
    all_derrame = Derrame.objects.all().order_by('-fecha_derrame')
    busqueda = request.GET.get("buscar")

    if busqueda:
        all_derrame = Derrame.objects.filter(
            Q(posicion__icontains = busqueda) |   
            Q(sustancia__icontains = busqueda) |         
            Q(empresa__icontains = busqueda) |
            Q(equipo__icontains = busqueda) |
            Q(estado__icontains = busqueda)

        ).distinct() 


    print(all_derrame)
    context = {
        'derrames':all_derrame,        
    }
    return render(request, 'derrame/list_derrame.html', context=context)

class DerrameDeleteView(LoginRequiredMixin,DeleteView):
    model = Derrame
    template_name = 'derrame/delete_derrame.html'
    success_url = '/DERRAMES/list_derrame/'

@login_required 
def derrame_update(request, pk):
    derrame = Derrame.objects.get(id=pk)

    if request.method == 'GET':        
        context = {
            'form': DerrameForm(
                initial={
                    'fecha_derrame':derrame.fecha_derrame,
                    'posicion':derrame.posicion,
                    'sustancia':derrame.sustancia,
                    'empresa':derrame.empresa,
                    'equipo':derrame.equipo,
                    'metros':derrame.metros,
                    'pintura_afectada':derrame.pintura_afectada,
                    'juntas':derrame.juntas,
                    'estado':derrame.estado,                    
                }
            )
        }
        return render(request, 'derrame/update_derrame.html', context=context)

    elif request.method == 'POST':
        form = DerrameForm(request.POST)
        if form.is_valid():
            derrame.fecha_derrame = form.cleaned_data['fecha_derrame']
            derrame.posicion = form.cleaned_data['posicion']
            derrame.sustancia = form.cleaned_data['sustancia']
            derrame.empresa = form.cleaned_data['empresa']
            derrame.equipo = form.cleaned_data['equipo']
            derrame.metros = form.cleaned_data['metros']
            derrame.pintura_afectada = form.cleaned_data['pintura_afectada']
            derrame.juntas = form.cleaned_data['juntas']            
            derrame.estado = form.cleaned_data['estado']
                       
            derrame.save()  

            context = {
                'message': 'DERRAME DE HIDROCARBUROS actualizado exitosamente'
            }
        else:
            context = {
                'form_errors': form.errors,
                'form': DerrameForm()
            }
        return render(request, 'derrame/update_derrame.html', context=context)