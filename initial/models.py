from django.db import models

class Initial(models.Model):
    initial_image = models.ImageField(upload_to= 'profile_images',null= True, blank= True)
    description = models.CharField(max_length=50, verbose_name= 'Descripcion',null= True, blank= True)
 
    def __str__(self):
        return self.description
        
    class Meta:
        verbose_name = 'Inicio'
        verbose_name_plural = 'Inicio'
