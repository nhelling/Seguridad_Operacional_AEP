from django.db import models

class Sms(models.Model):
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

    fecha = models.DateField(verbose_name= 'FECHA')
    evento = models.CharField(max_length=3000, verbose_name= 'EVENTO',choices= CONDITION_CHOICES_3)
    descripcion = models.CharField(max_length=3000, verbose_name= 'DESCRIPCION')
    mitigacion = models.CharField(max_length=3000, verbose_name= 'MEDIDAS MITIGACION ADOPTADAS')
    estado = models.CharField(max_length= 15, verbose_name= 'ESTADO', choices= CONDITION_CHOICES_1)
    status = models.CharField(max_length= 30, verbose_name= 'STATUS', choices= CONDITION_CHOICES_2)
    seguimiento = models.CharField(max_length=3000, verbose_name= 'SEGUIMIENTO')
    image_sms = models.FileField(upload_to= 'image_sms',null= True, blank= True, verbose_name= 'RELEVAMIENTO FOTOGRAFICO')    
       
    def __str__(self):
        return self.status
    
    class Meta:
        verbose_name = 'SMS'
        verbose_name_plural = 'SMS'
