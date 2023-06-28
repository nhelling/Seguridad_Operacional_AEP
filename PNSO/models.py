from django.db import models

class Pnso(models.Model):
    CONDITION_CHOICES = [
        
        ('AA - NO CUENTA CON INFORMACION SUFICIENTE','AA'),
        ('BB - NO REQUIERE ACCION DE MITIGACION','BB'),
        ('CC - ACCION DE MITIGACION EN CURSO','CC '),
        ('DD - MITIGACION CONCLUIDA','DD'),
        ('NN - NO CORRESPONDE SER TRAMITADO COMO PNSO','NN'), 
    ]

    nro = models.IntegerField(verbose_name= 'ID')
    fecha_recibido = models.DateField(verbose_name='Fecha Recibido', blank= True, null = True)
    fecha_evento = models.DateField(verbose_name= 'Fecha Evento', blank= True, null = True)
    texto = models.CharField(max_length=3000, verbose_name='Texto', blank= True, null = True)
    fecha_respuesta = models.DateField(verbose_name='Fecha Respuesta', blank= True, null = True)
    estado = models.CharField(max_length=50, verbose_name='Estado', choices= CONDITION_CHOICES, blank= True, null = True)
    mitigacion = models.CharField (max_length=3000, verbose_name='Mitigacion', blank= True, null = True)
    cierre = models.CharField(max_length=10, verbose_name='Cierre', blank= True, null = True)   
    image_pnso = models.FileField(upload_to= 'image_pnso',null= True, blank= True)
       
    def __str__(self):
        return self.estado
    
    class Meta:
        verbose_name = 'PNSO'
        verbose_name_plural = 'PNSOs'
