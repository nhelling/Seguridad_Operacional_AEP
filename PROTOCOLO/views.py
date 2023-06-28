from django.shortcuts import render
from django.views.generic import DeleteView, ListView, CreateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q

from PROTOCOLO.models import Protocolo
from PROTOCOLO.forms import ProtocoloForm

class ProtocoloListView(LoginRequiredMixin,ListView):
    model = Protocolo
    template_name = 'protocolo/list_protocolo.html'

@login_required 
def list_protocolo(request):
    all_protocolo = Protocolo.objects.all().order_by('-fecha_protocolo')
    busqueda = request.GET.get("buscar")
    if busqueda:
        all_protocolo = Protocolo.objects.filter(
            Q(orden__icontains = busqueda) |            
            Q(titulo__icontains = busqueda) 

        ).distinct()  


    print(all_protocolo)
    context = {
        'protocolos':all_protocolo,        
    }
    return render(request, 'protocolo/list_protocolo.html', context=context)

class ProtocoloCreateView(LoginRequiredMixin,CreateView):
    model = Protocolo
    template_name = 'protocolo/create_protocolo_full.html'
    fields = '__all__'
    success_url = '/PROTOCOLO/list_protocolo/'

class ProtocoloDeleteView(LoginRequiredMixin,DeleteView):
    model = Protocolo
    template_name = 'protocolo/delete_protocolo.html'
    success_url = '/PROTOCOLO/list_protocolo/'

@login_required 
def protocolo_update(request, pk):
    protocolo = Protocolo.objects.get(id=pk)

    if request.method == 'GET':        
        context = {
            'form': ProtocoloForm(
                initial={
                    'fecha_protocolo':protocolo.fecha_protocolo,
                    'orden':protocolo.orden,
                    'titulo':protocolo.titulo,
                    'pdf':protocolo.pdf,                   
                }
            )
        }
        return render(request, 'protocolo/update_protocolo.html', context=context)

    elif request.method == 'POST':
        form = ProtocoloForm(request.POST, request.FILES)
        if form.is_valid():
            protocolo.fecha_protocolo = form.cleaned_data['fecha_protocolo']
            protocolo.orden = form.cleaned_data['orden']
            protocolo.titulo = form.cleaned_data['titulo']
            protocolo.pdf = form.cleaned_data['pdf']                   
            protocolo.save()  

            context = {
                'message': 'PROTOCOLO Y PROCEDEMIENTO actualizado exitosamente'
            }
        else:
            context = {
                'form_errors': form.errors,
                'form': ProtocoloForm()
            }
        return render(request, 'protocolo/update_protocolo.html', context=context)