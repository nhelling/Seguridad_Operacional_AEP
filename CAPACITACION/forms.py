from django import forms
from django.forms import Textarea
from .models import Capacitacion

class CapacitacionForm(forms.Form):
    fecha_capacitacion = forms.DateField(required= True, label='Fecha')
    orden = forms.IntegerField(required= True, label='Orden')
    titulo = forms.CharField(required= True, label='Titulo',widget=forms.TextInput(attrs={"size": "140"}))
    pdf = forms.FileField(required= False, label='PDF')
    

    class Meta:
        model = Capacitacion
        fields = ['Fecha','Orden','Titulo','PDF']