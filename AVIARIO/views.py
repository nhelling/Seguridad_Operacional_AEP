from django.shortcuts import render
from django.views.generic import DeleteView, ListView, CreateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q

from AVIARIO.models import Aviario
from AVIARIO.forms import AviarioForm


class AviarioCreateView(LoginRequiredMixin,CreateView):
    model = Aviario
    template_name = 'aviario/create_aviario_full.html'
    fields = '__all__'
    success_url = '/AVIARIO/list_aviario/'


class AviarioListView(LoginRequiredMixin,ListView):
    model = Aviario
    template_name = 'aviario/list_aviario.html'

@login_required
def list_aviario(request):
    all_aviario = Aviario.objects.all().order_by('-fecha_aviario')
    busqueda = request.GET.get("buscar")

    if busqueda:
        all_aviario = Aviario.objects.filter(
            Q(especie_ave__icontains = busqueda) |            
            Q(empresa__icontains = busqueda) |
            Q(equipo__icontains = busqueda) |
            Q(estado__icontains = busqueda)

        ).distinct() 


    print(all_aviario)
    context = {
        'aviarios':all_aviario,        
    }
    return render(request, 'aviario/list_aviario.html', context=context)


class AviarioDeleteView(LoginRequiredMixin,DeleteView):
    model = Aviario
    template_name = 'aviario/delete_aviario.html'
    success_url = '/AVIARIO/list_aviario/'

@login_required
def aviario_update(request, pk):
    aviario = Aviario.objects.get(id=pk)

    if request.method == 'GET':        
        context = {
            'form': AviarioForm(
                initial={
                    'fecha_aviario':aviario.fecha_aviario,
                    'especie_ave':aviario.especie_ave,
                    'empresa':aviario.empresa,
                    'equipo':aviario.equipo,
                    'estado':aviario.estado,                    
                }
            )
        }
        return render(request, 'aviario/update_aviario.html', context=context)

    elif request.method == 'POST':
        form = AviarioForm(request.POST, request.FILES)
        if form.is_valid():
            aviario.fecha_aviario = form.cleaned_data['fecha_aviario']
            aviario.especie_ave = form.cleaned_data['especie_ave']
            aviario.empresa = form.cleaned_data['empresa']
            aviario.equipo = form.cleaned_data['equipo']
            aviario.estado = form.cleaned_data['estado']
                       
            aviario.save()  

            context = {
                'message': 'REPORTE DE IMPACTO actualizado exitosamente'
            }
        else:
            context = {
                'form_errors': form.errors,
                'form': AviarioForm()
            }
        return render(request, 'aviario/update_aviario.html', context=context)