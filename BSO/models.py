from django.db import models

class Bso(models.Model):
    fecha_bso = models.DateField(verbose_name='Fecha')
    orden = models.IntegerField(verbose_name='Orden')
    titulo = models.CharField(max_length=1000, verbose_name='Titulo')
    pdf = models.FileField(upload_to= 'pdf',null= True, blank= True)

    def __str__(self):
        return self.titulo
    
    class Meta:
        verbose_name = 'BSO'
        verbose_name_plural = 'BSO'
