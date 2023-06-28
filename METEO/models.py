from django.db import models

class Meteorologia(models.Model):
    meteorologia = models.CharField(max_length=1000, verbose_name='meteorologia')
