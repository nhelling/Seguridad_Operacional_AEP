from django.shortcuts import render
from django.views.generic import DeleteView, ListView, CreateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q

from SMS.models import Sms
from SMS.forms import SmsForm

class SmsCreateView(LoginRequiredMixin,CreateView):
    model = Sms
    template_name = 'sms/create_sms_full.html'
    fields = '__all__'
    success_url = '/SMS/list_sms/'

@login_required 
def list_sms(request):
    all_sms = Sms.objects.all().order_by('-fecha')
    busqueda = request.GET.get("buscar")

    if busqueda:
        all_sms = Sms.objects.filter(
            Q(estado__icontains = busqueda) |            
            Q(status__icontains = busqueda) 

        ).distinct() 


    print(all_sms)
    context = {
        'smss':all_sms,        
    }
    return render(request, 'sms/list_sms.html', context=context)

class SmsDeleteView(LoginRequiredMixin,DeleteView):
    model = Sms
    template_name = 'sms/delete_sms.html'
    success_url = '/SMS/list_sms/'

@login_required 
def sms_update(request, pk):
    sms = Sms.objects.get(id=pk)

    if request.method == 'GET':        
        context = {
            'form': SmsForm(
                initial={
                    'fecha':sms.fecha,
                    'evento':sms.evento,
                    'descripcion':sms.descripcion,
                    'mitigacion':sms.mitigacion,
                    'estado':sms.estado,
                    'status':sms.status,
                    'seguimiento':sms.seguimiento,
                    'image_sms':sms.image_sms,                    
                }
            )
        }
        return render(request, 'sms/update_sms.html', context=context)

    elif request.method == 'POST':
        form = SmsForm(request.POST, request.FILES)
        if form.is_valid():
            sms.fecha = form.cleaned_data['fecha']
            sms.evento = form.cleaned_data['evento']
            sms.descripcion = form.cleaned_data['descripcion']
            sms.mitigacion = form.cleaned_data['mitigacion']
            sms.estado = form.cleaned_data['estado']
            sms.status = form.cleaned_data['status']
            sms.seguimiento = form.cleaned_data['seguimiento']
            sms.seguimiento = form.cleaned_data['seguimiento']
            sms.image_sms = form.cleaned_data['image_sms']            
            sms.save()  

            context = {
                'message': 'SMS actualizado exitosamente'
            }
        else:
            context = {
                'form_errors': form.errors,
                'form': SmsForm()
            }
        return render(request, 'sms/update_sms.html', context=context)
