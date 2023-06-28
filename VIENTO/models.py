from django.db import models

class Viento(models.Model):    
    viento = models.CharField(max_length=1000, verbose_name='Viento')
    

    def __str__(self):
        return self.viento
    
    class Meta:
        verbose_name = 'VIENTO'
        verbose_name_plural = 'VIENTOS'
