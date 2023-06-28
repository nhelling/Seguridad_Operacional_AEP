from django.shortcuts import render
from django.views.generic import DeleteView, ListView, CreateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q

from BSO.models import Bso
from BSO.forms import BsoForm

class BsoListView(LoginRequiredMixin,ListView):
    model = Bso
    template_name = 'bso/list_bso.html'

@login_required 
def list_bso(request):
    all_bso = Bso.objects.all().order_by('-fecha_bso')
    busqueda = request.GET.get("buscar")

    if busqueda:
        all_bso = Bso.objects.filter(
            Q(orden__icontains = busqueda) |            
            Q(titulo__icontains = busqueda) 

        ).distinct()  


    print(all_bso)
    context = {
        'bsos':all_bso,        
    }
    return render(request, 'bso/list_bso.html', context=context)

class BsoCreateView(LoginRequiredMixin,CreateView):
    model = Bso
    template_name = 'bso/create_bso_full.html'
    fields = '__all__'
    success_url = '/BSO/list_bso/'

class BsoDeleteView(LoginRequiredMixin,DeleteView):
    model = Bso
    template_name = 'bso/delete_bso.html'
    success_url = '/BSO/list_bso/'

@login_required 
def bso_update(request, pk):
    bso = Bso.objects.get(id=pk)

    if request.method == 'GET':        
        context = {
            'form': BsoForm(
                initial={
                    'fecha_bso':bso.fecha_bso,
                    'orden':bso.orden,
                    'titulo':bso.titulo,
                    'pdf':bso.pdf,                   
                }
            )
        }
        return render(request, 'bso/update_bso.html', context=context)

    elif request.method == 'POST':
        form = BsoForm(request.POST, request.FILES)
        if form.is_valid():
            bso.fecha_bso = form.cleaned_data['fecha_bso']
            bso.orden = form.cleaned_data['orden']
            bso.titulo = form.cleaned_data['titulo']
            bso.pdf = form.cleaned_data['pdf']                   
            bso.save()  

            context = {
                'message': 'BSO actualizado exitosamente'
            }
        else:
            context = {
                'form_errors': form.errors,
                'form': BsoForm()
            }
        return render(request, 'bso/update_bso.html', context=context)