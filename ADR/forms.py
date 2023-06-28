from django import forms
from django.forms import Textarea
from .models import Adr

class AdrForm(forms.Form):
    CONDITION_CHOICES_ESTADO = [
        ('PRESENTADO','PRESENTADO'),
        ('APROBADO','APROBADO'),
    ]
    
    fecha_presentado = forms.DateField(required= True, label='Fecha_Presentado')
    titulo = forms.CharField(required= True, label='Titulo',widget=forms.TextInput(attrs={"size": "140"}))
    fecha_aprobado = forms.DateField(required= False, label='Fecha_Aprobado')
    estado = forms.CharField(required= True, label='Estado', widget=forms.Select(choices=CONDITION_CHOICES_ESTADO))
    archivo = forms.FileField(required= False, label='Archivo')
    

    class Meta:
        model = Adr
        fields = ['Fecha_Presentado','Titulo','Fecha_Aprobado','Estado' ,'Archivo']