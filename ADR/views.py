from django.shortcuts import render
from django.views.generic import DeleteView, ListView, CreateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q

from ADR.models import Adr
from ADR.forms import AdrForm

class AdrListView(LoginRequiredMixin,ListView):
    model = Adr
    template_name = 'adr/list_adr.html'
    
@login_required 
def list_adr(request):
    all_adr = Adr.objects.all().order_by('-fecha_presentado')
    busqueda = request.GET.get("buscar")

    if busqueda:
        all_adr = Adr.objects.filter(
            Q(titulo__icontains = busqueda) |            
            Q(estado__icontains = busqueda) |
            Q(fecha_presentado__icontains = busqueda) 

        ).distinct()  


    print(all_adr)
    context = {
        'adrs':all_adr,        
    }
    return render(request, 'adr/list_adr.html', context=context)

class AdrCreateView(LoginRequiredMixin,CreateView):
    model = Adr
    template_name = 'adr/create_adr_full.html'
    fields = '__all__'
    success_url = '/ADR/list_adr/'
    
class AdrDeleteView(LoginRequiredMixin,DeleteView):
    model = Adr
    template_name = 'adr/delete_adr.html'
    success_url = '/ADR/list_adr/'
    
@login_required 
def adr_update(request, pk):
    adr = Adr.objects.get(id=pk)

    if request.method == 'GET':        
        context = {
            'form': AdrForm(
                initial={
                    'fecha_presentado':adr.fecha_presentado,
                    'titulo':adr.titulo,
                    'fecha_aprobado':adr.fecha_aprobado,
                    'estado':adr.estado,
                    'archivo':adr.archivo,                   
                }
            )
        }
        return render(request, 'adr/update_adr.html', context=context)

    elif request.method == 'POST':
        form = AdrForm(request.POST, request.FILES)
        if form.is_valid():
            adr.fecha_presentado = form.cleaned_data['fecha_presentado']
            adr.titulo = form.cleaned_data['titulo']
            adr.fecha_aprobado = form.cleaned_data['fecha_aprobado']
            adr.estado = form.cleaned_data['estado']
            adr.archivo = form.cleaned_data['archivo']                   
            adr.save()  

            context = {
                'message': 'ADR actualizado exitosamente'
            }
        else:
            context = {
                'form_errors': form.errors,
                'form': AdrForm()
            }
        return render(request, 'adr/update_adr.html', context=context)
    
    