from django import forms
from django.forms import Textarea
from .models import Pnso
from django.db import models

class PnsoForm(forms.Form):
    
    CONDITION_CHOICES = [
        
        ('AA','A-NO CUENTA CON INFORMACION SUFICIENTE'),
        ('BB','B-NO REQUIERE ACCION DE MITIGACION'),
        ('CC','C-ACCION DE MITIGACION EN CURSO'),
        ('DD','D-MITIGACION CONCLUIDA'),
        ('NN','N-NO CORRESPONDE SER TRAMITADO COMO PNSO'), 
    ]
      
    nro = forms.IntegerField(required= True, label='Nro')
    fecha_recibido = forms.DateField(required= True, label='Fecha Recibido')
    fecha_evento = forms.DateField(required= True, label='Fecha Evento')
    texto = forms.CharField(required= False, label='Texto',widget=forms.TextInput(attrs={"size": "140"}))
    fecha_respuesta = forms.DateField(required= False, label='Fecha Respuesta')
    estado = forms.CharField(required= True, label='Estado', widget=forms.Select(choices=CONDITION_CHOICES) )
    mitigacion = forms.CharField (required= False, label='Mitigacion',widget=forms.TextInput(attrs={"size": "140"}))
    cierre = forms.CharField(required= True, label='Cierre') 
    image_pnso = forms.ImageField(required= False, label='Foto') 

    class Meta:
        model = Pnso
        fields = ['nro','fecha_recibido','fecha_evento','texto','fecha_respuesta','estado','mitigacion','cierre','image_pnso']
       