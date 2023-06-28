from django.db import models

class Mapa(models.Model):    
    mapa = models.CharField(max_length=1000, verbose_name='Mapa')
    

    def __str__(self):
        return self.mapa
    
    class Meta:
        verbose_name = 'MAPA'
        verbose_name_plural = 'MAPAS'
