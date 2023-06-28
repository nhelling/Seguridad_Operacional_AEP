from django import forms
from django.forms import Textarea
from .models import Bso

class BsoForm(forms.Form):
    fecha_bso = forms.DateField(required= True, label='Fecha')
    orden = forms.IntegerField(required= True, label='Orden')
    titulo = forms.CharField(required= True, label='Titulo',widget=forms.TextInput(attrs={"size": "140"}))
    pdf = forms.FileField(required= False, label='PDF')
    

    class Meta:
        model = Bso
        fields = ['Fecha','Orden','Titulo','PDF']
       