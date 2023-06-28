from django import forms
from django.forms import Textarea
from .models import Sms

class SmsForm(forms.Form):
    
    CONDITION_CHOICES_1 = [
        ('ABIERTO','ABIERTO'), 
        ('CERRADO','CERRADO'), 

    ]  

    CONDITION_CHOICES_2 = [
        ('REQUIERE SEGUIMIENTO','REQUIERE SEGUIMIENTO'), 
        ('NO REQUIERE SEGUIMIENTO','NO REQUIERE SEGUIMIENTO'), 

    ] 

    CONDITION_CHOICES_3 = [
        ('-------------------','-'),
        ('BACHEO / DESPRENDIMIENTOS','BACHEO / DESPRENDIMIENTOS'),
        ('COLISION DE AERONAVE Y VEHICULO TERRESTRE','COLISION DE AERONAVE Y VEHICULO TERRESTRE'),
        ('COLISION DE AERONAVES','COLISION DE AERONAVES'),
        ('COLISION EQUIPOS TERRESTRES','COLISION EQUIPOS TERRESTRES'),
        ('DEFICIENCIAS BALIZAMIENTO ','DEFICIENCIAS BALIZAMIENTO '),
        ('DERRAMES DE HIDROCARBUROS','DERRAMES DE HIDROCARBUROS'),
        ('EXCURSION DE PISTA','EXCURSION DE PISTA'),
        ('FALTANTES','FALTANTES'),
        ('FOCO IGNEO','FOCO IGNEO'),
        ('FOD EN PISTA','FOD EN PISTA'), 
        ('IMPACTO CON AVE','IMPACTO CON AVE'),    
        ('INCURSION EN PISTA','INCURSION EN PISTA'),
        ('INTRUSION DE PERSONAS','INTRUSION DE PERSONAS'),
        ('PNSO','PNSO'), 
        ('SEÑALETICA HORIZONTAL','SEÑALETICA HORIZONTAL'), 
        ('SEÑALETICA VERTICAL','SEÑALETICA VERTICAL'),
        ('VANDALISMO CERCO','VANDALISMO CERCO'),
        ('VEHICULO PENALIZANDO POSICION','VEHICULO PENALIZANDO POSICION'), 

    ]
    
    
    
    fecha = forms.DateField(required= True, label= 'FECHA')
    evento = forms.CharField(required= True, label= 'EVENTO', widget=forms.Select(choices=CONDITION_CHOICES_3))
    descripcion = forms.CharField(required= True, label= 'DESCRIPCION',widget=forms.TextInput(attrs={"size": "140"}))
    mitigacion = forms.CharField(required= True, label= 'MEDIDAS MITIGACION ADOPTADAS',widget=forms.TextInput(attrs={"size": "140"}))
    estado = forms.CharField(required= True, label= 'ESTADO', widget=forms.Select(choices=CONDITION_CHOICES_1))
    status = forms.CharField(required= True, label= 'STATUS', widget=forms.Select(choices=CONDITION_CHOICES_2))
    seguimiento = forms.CharField(required= True, label= 'SEGUIMIENTO')
    image_sms = forms.ImageField(required= False, label='RELEVAMIENTO FOTOGRAFICO')     

    class Meta:
        model = Sms
        fields = ['fecha','evento','descripcion','mitigacion','estado','status','seguimiento','image_sms']




   
       