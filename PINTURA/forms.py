from django import forms
from django.forms import Textarea
from .models import Pintura

class PinturaForm(forms.Form):
    CONDITION_CHOICES_1 = [        
        ('EJE INGRESO','EJE INGRESO'),
        ('INDICADOR POSICION','INDICADOR POSICION'),
        ('INDICADOR STOP BAR','INDICADOR STOP BAR'),  
        ('INDICADOR POSICION / STOP BAR','INDICADOR POSICION / STOP BAR'),      
        ('N/A','N/A'),
        ('CEBRADO','CEBRADO'),
        ('COMPLETA','COMPLETA'),
        ('PUNTO PARKING PASARELA','PUNTO PARKING PASARELA'),
        ('ROJO Y BLANCO','ROJO Y BLANCO'),
    ]
    
    CONDITION_CHOICES_2 = [                
        ('ABIERTO','ABIERTO'),
        ('CERRADO','CERRADO'),        
    ]
    
    CONDITION_CHOICES_3 = [                                  
        ('01','01'),
        ('02','02'),
        ('PAS-03','PAS-03'),
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
    
    CONDITION_CHOICES_4 = [              
        ('% 33','% 33'),
        ('% 50','% 50'), 
        ('% 75','% 75'), 
        ('% 100','% 100'),       
    ]
    
    CONDITION_CHOICES_5 = [              
        ('PLAT. COMERCIAL','PLAT. COMERCIAL'),  
        ('PLAT. INDUSTRIAL','PLAT. INDUSTRIAL'),
        ('PLAT. SUR','PLAT. SUR'),       
    ]
    CHOICES = [
        ('EJE INGRESO','EJE INGRESO'),
        ('INDICADOR POSICION','INDICADOR POSICION'),
        ('INDICADOR STOP BAR','INDICADOR STOP BAR'),  
        ('INDICADOR POSICION / STOP BAR','INDICADOR POSICION / STOP BAR'),      
        ('N/A','N/A'),
        ('CEBRADO','CEBRADO'),
        ('COMPLETA','COMPLETA'),
        ('PUNTO PARKING PASARELA','PUNTO PARKING PASARELA'),
        ('ROJO Y BLANCO','ROJO Y BLANCO'),
    ]
    
    fecha_pos = forms.DateField(required= True, label='Fecha')
    posicion = forms.CharField(required= True, label='Posicion', widget=forms.Select(choices=CONDITION_CHOICES_3))
    lineas_de_guia = forms.CharField(required= True, label='Lineas de Guia', widget=forms.Select(choices=CONDITION_CHOICES_1))
    #lineas_de_guia = forms.ChoiceField( choices=[CHOICES], required=False,label='Lineas de Guia')
    fecha_carteleria = forms.DateField(required= False, label='Fecha')
    carteleria = forms.CharField(required= False, label='Carteleria', widget=forms.Select(choices=CONDITION_CHOICES_1))
    fecha_lineas_seguridad = forms.DateField(required= True, label='Fecha')
    lineas_seguridad = forms.CharField (required= False, label='Lineas de Seguridad', widget=forms.Select(choices=CONDITION_CHOICES_1))
    sector = forms.CharField(required= True, label='Sector', widget=forms.Select(choices=CONDITION_CHOICES_5)) 
    pintado = forms.CharField(required= True, label='Pintado', widget=forms.Select(choices=CONDITION_CHOICES_4)) 
    estado = forms.CharField(required= False, label='Estado', widget=forms.Select(choices=CONDITION_CHOICES_2)) 

    class Meta:
        model = Pintura
        fields = ['fecha_pos','posicion','lineas_de_guia','fecha_carteleria','carteleria','fecha_lineas_seguridad','lineas_seguridad','sector','pintado','estado']
    