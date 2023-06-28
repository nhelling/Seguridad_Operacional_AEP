from django.db import models

class Aviario(models.Model):
    CONDITION_CHOICES_ESPECIE = [
        ('CERNICALO','CERNICALO'),
        ('CHIMANGO','CHIMANGO'),
        ('GOLONDRINA','GOLONDRINA'), 
        ('HALCONCITO COLORADO','HALCONCITO COLORADO'),
        ('LECHUZA','LECHUZA'),  
        ('MURCIELAGO','MURCIELAGO'), 
        ('PALOMA TORCAZA','PALOMA TORCAZA'),     
        ('TERO','TERO'), 
        ('OTROS','OTROS'), 
        ('SIN EVIDENCIA','SIN EVIDENCIA'),  

    ]

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

    CONDITION_CHOICES_ESTADO = [
        ('ABIERTO','ABIERTO'),
        ('CERRADO','CERRADO'),   
    ]

    fecha_aviario = models.DateField(verbose_name= 'Fecha')
    especie_ave = models.CharField(max_length=100, verbose_name='Especie Aves', choices= CONDITION_CHOICES_ESPECIE)
    empresa = models.CharField(max_length=50, verbose_name='Empresa', choices=CONDITION_CHOICES_EMPRESA)
    equipo = models.CharField(max_length=8, verbose_name='Equipo')
    estado = models.CharField(max_length=10, verbose_name='Estado', choices=CONDITION_CHOICES_ESTADO)

    def __str__(self):
        return self.estado
    
    class Meta:
        verbose_name = 'IMPACTO'
        verbose_name_plural = 'IMPACTOS'
        