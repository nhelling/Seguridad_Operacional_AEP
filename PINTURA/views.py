from django.shortcuts import render
from django.views.generic import DeleteView, ListView, CreateView, UpdateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q

from PINTURA.models import Pintura
from PINTURA.forms import PinturaForm

@login_required 
def list_pintura(request):
    all_pintura = Pintura.objects.all().order_by('-fecha_pos')
    busqueda = request.GET.get("buscar")

    if busqueda:
        all_pintura = Pintura.objects.filter(
            Q(posicion__icontains = busqueda) |            
            Q(estado__icontains = busqueda) 

        ).distinct()    

    print(all_pintura)
    context = {
        'pinturas':all_pintura,   
             
    }
    return render(request, 'pintura/list_pintura.html', context=context)

class PinturaCreateView(LoginRequiredMixin,CreateView):
    model = Pintura
    template_name = 'pintura/create_pintura_full.html'
    fields = '__all__'
    success_url = '/PINTURA/list_pintura/'

class PinturaDeleteView(LoginRequiredMixin,DeleteView):
    model = Pintura
    template_name = 'pintura/delete_pintura.html'
    success_url = '/PINTURA/list_pintura/'
    
class PinturaUpdateView(LoginRequiredMixin,UpdateView):
   model=Pintura
   fields="__all__"
   template_name='pintura/update_pintura.html'
   success_url='/PINTURA/list_pintura/'

@login_required 
def pintura_update(request, pk):
    pintura = Pintura.objects.get(id=pk)

    if request.method == 'GET':        
        context = {
            'form': PinturaForm(
                initial={
                    'fecha_pos':pintura.fecha_pos,
                    'posicion':pintura.posicion,
                    'lineas_de_guia':pintura.lineas_de_guia,
                    'fecha_carteleria':pintura.fecha_carteleria,
                    'carteleria':pintura.carteleria,
                    'fecha_lineas_seguridad':pintura.fecha_lineas_seguridad,
                    'lineas_seguridad':pintura.lineas_seguridad,
                    'sector':pintura.sector,
                    'pintado':pintura.pintado,
                    'estado':pintura.estado,
                }
            )
        }
        return render(request, 'pintura/update_pintura.html', context=context)

    elif request.method == 'POST':
        form = PinturaForm(request.POST)
        if form.is_valid():
            pintura.fecha_pos = form.cleaned_data['fecha_pos']
            pintura.posicion = form.cleaned_data['posicion']
            pintura.lineas_de_guia = form.cleaned_data['lineas_de_guia']
            pintura.fecha_carteleria = form.cleaned_data['fecha_carteleria']
            pintura.carteleria = form.cleaned_data['carteleria']
            pintura.fecha_lineas_seguridad = form.cleaned_data['fecha_lineas_seguridad']
            pintura.lineas_seguridad = form.cleaned_data['lineas_seguridad']
            pintura.sector = form.cleaned_data['sector']
            pintura.pintado = form.cleaned_data['pintado'] 
            pintura.estado = form.cleaned_data['estado']            
            pintura.save()  

            context = {
                'message': 'PINTURA actualizada exitosamente'
            }
        else:
            context = {
                'form_errors': form.errors,
                'form': PinturaForm()
            }
        return render(request, 'pintura/update_pintura.html', context=context)


