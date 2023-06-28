from django.shortcuts import render
from django.views.generic import DeleteView, ListView, CreateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q

from PNSO.models import Pnso
from PNSO.forms import PnsoForm

class PnsoCreateView(LoginRequiredMixin,CreateView):
    model = Pnso
    template_name = 'pnso/create_pnso_full.html'
    fields = '__all__'
    success_url = '/PNSO/list_pnso/'

class PnsoListView(LoginRequiredMixin,ListView):
    model = Pnso
    template_name = 'pnso/list_pnso.html'

@login_required 
def list_pnso(request):
    all_pnso = Pnso.objects.all().order_by('-fecha_recibido')
    busqueda = request.GET.get("buscar")

    if busqueda:
        all_pnso = Pnso.objects.filter(
            Q(nro__icontains = busqueda) |            
            Q(estado__icontains = busqueda) |
            Q(cierre__icontains = busqueda)

        ).distinct() 


    print(all_pnso)
    context = {
        'pnsos':all_pnso,        
    }
    return render(request, 'pnso/list_pnso.html', context=context)

class PnsoDeleteView(LoginRequiredMixin,DeleteView):
    model = Pnso
    template_name = 'pnso/delete_pnso.html'
    success_url = '/PNSO/list_pnso/'

@login_required 
def pnso_update(request, pk):
    pnso = Pnso.objects.get(id=pk)

    if request.method == 'GET':        
        context = {
            'form': PnsoForm(
                initial={
                    'nro':pnso.nro,
                    'fecha_recibido':pnso.fecha_recibido,
                    'fecha_evento':pnso.fecha_evento,
                    'texto':pnso.texto,
                    'fecha_respuesta':pnso.fecha_respuesta,
                    'estado':pnso.estado,
                    'mitigacion':pnso.mitigacion,
                    'cierre':pnso.cierre,
                    'image_pnso':pnso.image_pnso,
                }
            )
        }
        return render(request, 'pnso/update_pnso.html', context=context)

    elif request.method == 'POST':
        form = PnsoForm(request.POST, request.FILES)
        if form.is_valid():
            pnso.nro = form.cleaned_data['nro']
            pnso.fecha_recibido = form.cleaned_data['fecha_recibido']
            pnso.fecha_evento = form.cleaned_data['fecha_evento']
            pnso.texto = form.cleaned_data['texto']
            pnso.fecha_respuesta = form.cleaned_data['fecha_respuesta']
            pnso.estado = form.cleaned_data['estado']
            pnso.mitigacion = form.cleaned_data['mitigacion']
            pnso.cierre = form.cleaned_data['cierre']
            pnso.image_pnso = form.cleaned_data['image_pnso']            
            pnso.save()  

            context = {
                'message': 'PNSO actualizado exitosamente'
            }
        else:
            context = {
                'form_errors': form.errors,
                'form': PnsoForm()
            }
        return render(request, 'pnso/update_pnso.html', context=context)
