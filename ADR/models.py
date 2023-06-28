from django.db import models

class Adr(models.Model):
    
    CONDITION_CHOICES_ESTADO = [
        ('PRESENTADO','PRESENTADO'),
        ('APROBADO','APROBADO'),
    ]
    
    fecha_presentado = models.DateField(verbose_name= 'Fecha Presentado', blank= True, null = True)
    titulo = models.CharField(max_length=300, verbose_name= 'Titulo', blank= True, null = True)
    fecha_aprobado = models.DateField(verbose_name= 'Fecha Aprobado', blank= True, null = True)
    estado = models.CharField(max_length=20, verbose_name='Estado', choices= CONDITION_CHOICES_ESTADO, default='PRESENTADO', blank= True, null = True)
    archivo = models.FileField(upload_to= 'archivo',null= True, blank= True)
    
    def __str__(self):
        return self.titulo
    
    class Meta:
        verbose_name = 'ADR'
        verbose_name_plural = 'ADRs'
