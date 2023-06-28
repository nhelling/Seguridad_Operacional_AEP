from django import forms
from django.forms import Textarea
from .models import Derrame

class DerrameForm(forms.Form):
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

    CONDITION_CHOICES_SUSTANCIA = [
        ('COMBUSTIBLE AERONAUTICO','COMBUSTIBLE AERONAUTICO'), 
        ('COMBUSTIBLE TERRESTRE','COMBUSTIBLE TERRESTRE'),
        ('LIQUIDO HIDRAULICO','LIQUIDO HIDRAULICO'),
        ('ACEITES TERRESTRES','ACEITES TERRESTRES'),
        ('ACEITES AERONAUTICOS','ACEITES AERONAUTICOS'),
        ('OTROS','OTROS'),        

    ] 

    CONDITION_CHOICES_ESTADO = [
        ('ABIERTO','ABIERTO'),
        ('CERRADO','CERRADO'),   
    ]
    
    CONDITION_CHOICES_POSICION = [                                  
        ('01','01'),
        ('02','02'),
        ('PAS-03','PAS-03'),
        ('PAS-03A','PAS-03A'),
        ('PAS-03C','PAS-03C'),
        ('PAS-04','PAS-04'),
        ('PAS-05','PAS-05'),
        ('PAS-06','PAS-06'),
        ('PAS-07','PAS-07'),
        ('PAS-08','PAS-08'),
        ('PAS-09','PAS-09'),
        ('PAS-10','PAS-10'),
        ('PAS-11','PAS-11'),
        ('PAS-12','PAS-12'),
        ('13','13'),
        ('14','14'),
        ('15','15'),
        ('16','16'),
        ('17','17'),
        ('18','18'),
        ('19','19'),
        ('20','20'),
        ('21','21'),
        ('22','22'),
        ('23','23'),
        ('24','24'),
        ('25','25'),
        ('26','26'),
        ('27','27'),
        ('28','28'),
        ('29','29'),
        ('30','30'),
        ('31','31'),
        ('32A','32A'),
        ('32B','32B'),
        ('32C','32C'),
        ('67','67'),
        ('68','68'),
        ('69','69'),
        ('39','39'),
        ('39A','39A'),
        ('40','40'),
        ('41','41'),
        ('42','42'),
        ('43','43'),
        ('44','44'),
        ('45','45'),
        ('46','46'),
        ('47','47'),
        ('48','48'),
        ('49','49'),
        ('50','50'),
        ('51','51'),
        ('66','66'),        
    ]
    fecha_derrame = forms.DateField(required= True, label='Fecha')
    posicion = forms.CharField(required= True, label='Posicion', widget=forms.Select(choices=CONDITION_CHOICES_POSICION))
    sustancia = forms.CharField(required= True, label='Sustancia', widget=forms.Select(choices=CONDITION_CHOICES_SUSTANCIA))
    empresa = forms.CharField(required= True, label='Empresa', widget=forms.Select(choices=CONDITION_CHOICES_EMPRESA))
    equipo = forms.CharField(required= False, label='Equipo')
    metros = forms.CharField(required= True, label='Metros Afectados')
    pintura_afectada = forms.CharField(required= True, label='Pintura Afectada')
    juntas = forms.CharField(required= True, label='Juntas Afectadas')
    estado = forms.CharField(required= True, label='Estado', widget=forms.Select(choices=CONDITION_CHOICES_ESTADO))

    class Meta:
        model = Derrame
        fields = ['Fecha','Posicion','Sustancia','Empresa','Equipo','Metros Afectados','Pintura Afectada','Juntas Afectadas','Estado']