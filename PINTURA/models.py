from django.db import models

class Pintura(models.Model):
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
        ('PAS-03A','PAS-03A'),
        ('PAS-03C','PAS-03C'),
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
        ('32A','32A'),
        ('32B','32B'),
        ('32C','32C'),
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
    
    
    fecha_pos = models.DateField(verbose_name='Fecha')
    posicion = models.CharField(max_length=10, verbose_name='POS', choices=CONDITION_CHOICES_3)
    lineas_de_guia = models.CharField(max_length=100, verbose_name='Lineas de Guia',choices=CONDITION_CHOICES_1,null= True, blank= True)
    fecha_carteleria = models.DateField(verbose_name='Fecha')
    carteleria = models.CharField(max_length=100, verbose_name='Carteleria',choices=CONDITION_CHOICES_1,null= True, blank= True)
    fecha_lineas_seguridad = models.DateField(verbose_name='Fecha')
    lineas_seguridad = models.CharField(max_length=100, verbose_name='Lineas de Seguridad',choices=CONDITION_CHOICES_1,null= True, blank= True)
    sector = models.CharField(max_length=50, verbose_name='Sector',choices=CONDITION_CHOICES_5)
    pintado = models.CharField(max_length=10, verbose_name='% Pintado',choices=CONDITION_CHOICES_4)
    estado = models.CharField(max_length=20, verbose_name='Estado',choices=CONDITION_CHOICES_2)

    def __str__(self):
        return self.posicion
    
    class Meta:
        verbose_name = 'PINTURA'
        verbose_name_plural = 'PINTURA'