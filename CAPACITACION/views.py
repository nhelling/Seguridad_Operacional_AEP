from django.shortcuts import render
from django.views.generic import DeleteView, ListView, CreateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q

from CAPACITACION.models import Capacitacion
from CAPACITACION.forms import CapacitacionForm

class CapacitacionListView(LoginRequiredMixin,ListView):
    model = Capacitacion
    template_name = 'capacitacion/list_capacitacion.html'

@login_required 
def list_capacitacion(request):
    all_capacitacion = Capacitacion.objects.all().order_by('-fecha_capacitacion')
    busqueda = request.GET.get("buscar")

    if busqueda:
        all_capacitacion = Capacitacion.objects.filter(
            Q(orden__icontains = busqueda) |            
            Q(titulo__icontains = busqueda) 

        ).distinct()  


    print(all_capacitacion)
    context = {
        'capacitaciones':all_capacitacion,        
    }
    return render(request, 'capacitacion/list_capacitacion.html', context=context)

class CapacitacionCreateView(LoginRequiredMixin,CreateView):
    model = Capacitacion
    template_name = 'capacitacion/create_capacitacion_full.html'
    fields = '__all__'
    success_url = '/CAPACITACION/list_capacitacion/'

class CapacitacionDeleteView(LoginRequiredMixin,DeleteView):
    model = Capacitacion
    template_name = 'capacitacion/delete_capacitacion.html'
    success_url = '/CAPACITACION/list_capacitacion/'

@login_required 
def capacitacion_update(request, pk):
    capacitacion = Capacitacion.objects.get(id=pk)

    if request.method == 'GET':        
        context = {
            'form': CapacitacionForm(
                initial={
                    'fecha_capacitacion':capacitacion.fecha_capacitacion,
                    'orden':capacitacion.orden,
                    'titulo':capacitacion.titulo,
                    'pdf':capacitacion.pdf,                   
                }
            )
        }
        return render(request, 'capacitacion/update_capacitacion.html', context=context)

    elif request.method == 'POST':
        form = CapacitacionForm(request.POST, request.FILES)
        if form.is_valid():
            capacitacion.fecha_capacitacion = form.cleaned_data['fecha_capacitacion']
            capacitacion.orden = form.cleaned_data['orden']
            capacitacion.titulo = form.cleaned_data['titulo']
            capacitacion.pdf = form.cleaned_data['pdf']                   
            capacitacion.save()  

            context = {
                'message': 'CAPACITACION actualizada exitosamente'
            }
        else:
            context = {
                'form_errors': form.errors,
                'form': CapacitacionForm()
            }
        return render(request, 'capacitacion/update_capacitacion.html', context=context)