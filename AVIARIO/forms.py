from django import forms
from django.forms import Textarea
from .models import Aviario

class AviarioForm(forms.Form):
    CONDITION_CHOICES_ESPECIE = [
        ('CERNICALO','CERNICALO'),
        ('CHIMANGO','CHIMANGO'),
        ('GOLONDRINA','GOLONDRINA'), 
        ('HALCONCITO COLORADO','HALCONCITO COLORADO'),
        ('LECHUZA','LECHUZA'),  
        ('MURCIELAGO','MURCIELAGO'), 
        ('PALOMA TORCAZA','PALOMA TORCAZA'),     
        ('TERO','TERO'), 
        ('OTROS','OTROS'), 
        ('SIN EVIDENCIA','SIN EVIDENCIA'),  

    ]

    CONDITION_CHOICES_EMPRESA = [
        ('5U - LADE','5U'), 
        ('AJ - AMERICAN JET','AJ'), 
        ('AR - ARSA','AR'), 
        ('FO - FLYBONDI','FO'), 
        ('G3 - GOL','G3'), 
        ('H2 - SKY','H2'), 
        ('JA - JETSMART CHILE','JA'), 
        ('JJ - LATAM BRASIL','JJ'), 
        ('LA - LATAM AIRLINES','LA'), 
        ('LP - LATAM PERU ','LP'), 
        ('WJ - JETSMART ARGENTINA ','WJ'), 
        ('ZP - PARANAIR ','ZP'), 
        ('PRV - AV. GENERAL ','PRV'),   

    ]   

    CONDITION_CHOICES_ESTADO = [
        ('ABIERTO','ABIERTO'),
        ('CERRADO','CERRADO'),   
    ]
    
    fecha_aviario = forms.DateField(required= True, label='Fecha')
    especie_ave = forms.CharField(required= True, label='Especie Ave', widget=forms.Select(choices=CONDITION_CHOICES_ESPECIE))
    empresa = forms.CharField(required= True, label='Empresa', widget=forms.Select(choices=CONDITION_CHOICES_EMPRESA))
    equipo = forms.CharField(required= False, label='Equipo')
    estado = forms.CharField(required= True, label='Estado', widget=forms.Select(choices=CONDITION_CHOICES_ESTADO))

    class Meta:
        model = Aviario
        fields = ['Fecha','Especie Ave','Empresa','Equipo','Estado']