# Generated by Django 4.1.3 on 2023-03-14 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PINTURA', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pintura',
            name='carteleria',
            field=models.CharField(blank=True, choices=[('EJE INGRESO', 'EJE INGRESO'), ('INDICADOR POSICION', 'INDICADOR POSICION'), ('INDICADOR STOP BAR', 'INDICADOR STOP BAR'), ('INDICADOR POSICION / STOP BAR', 'INDICADOR POSICION / STOP BAR'), ('N/A', 'N/A'), ('CEBRADO', 'CEBRADO'), ('COMPLETA', 'COMPLETA'), ('PUNTO PARKING PASARELA', 'PUNTO PARKING PASARELA'), ('ROJO Y BLANCO', 'ROJO Y BLANCO')], max_length=100, null=True, verbose_name='Carteleria'),
        ),
        migrations.AlterField(
            model_name='pintura',
            name='estado',
            field=models.CharField(choices=[('ABIERTO', 'ABIERTO'), ('CERRADO', 'CERRADO')], max_length=20, verbose_name='Estado'),
        ),
        migrations.AlterField(
            model_name='pintura',
            name='lineas_de_guia',
            field=models.CharField(blank=True, choices=[('EJE INGRESO', 'EJE INGRESO'), ('INDICADOR POSICION', 'INDICADOR POSICION'), ('INDICADOR STOP BAR', 'INDICADOR STOP BAR'), ('INDICADOR POSICION / STOP BAR', 'INDICADOR POSICION / STOP BAR'), ('N/A', 'N/A'), ('CEBRADO', 'CEBRADO'), ('COMPLETA', 'COMPLETA'), ('PUNTO PARKING PASARELA', 'PUNTO PARKING PASARELA'), ('ROJO Y BLANCO', 'ROJO Y BLANCO')], max_length=100, null=True, verbose_name='Lineas de Guia'),
        ),
        migrations.AlterField(
            model_name='pintura',
            name='lineas_seguridad',
            field=models.CharField(blank=True, choices=[('EJE INGRESO', 'EJE INGRESO'), ('INDICADOR POSICION', 'INDICADOR POSICION'), ('INDICADOR STOP BAR', 'INDICADOR STOP BAR'), ('INDICADOR POSICION / STOP BAR', 'INDICADOR POSICION / STOP BAR'), ('N/A', 'N/A'), ('CEBRADO', 'CEBRADO'), ('COMPLETA', 'COMPLETA'), ('PUNTO PARKING PASARELA', 'PUNTO PARKING PASARELA'), ('ROJO Y BLANCO', 'ROJO Y BLANCO')], max_length=100, null=True, verbose_name='Lineas de Seguridad'),
        ),
        migrations.AlterField(
            model_name='pintura',
            name='pintado',
            field=models.CharField(choices=[('% 33', '% 33'), ('% 50', '% 50'), ('% 75', '% 75'), ('% 100', '% 100')], max_length=10, verbose_name='% Pintado'),
        ),
        migrations.AlterField(
            model_name='pintura',
            name='posicion',
            field=models.CharField(choices=[('01', '01'), ('02', '02'), ('PAS-03', 'PAS-03'), ('PAS-04', 'PAS-04'), ('PAS-05', 'PAS-05'), ('PAS-06', 'PAS-06'), ('PAS-07', 'PAS-07'), ('PAS-08', 'PAS-08'), ('PAS-09', 'PAS-09'), ('PAS-10', 'PAS-10'), ('PAS-11', 'PAS-11'), ('PAS-12', 'PAS-12'), ('13', '13'), ('14', '14'), ('15', '15'), ('16', '16'), ('17', '17'), ('18', '18'), ('19', '19'), ('20', '20'), ('21', '21'), ('22', '22'), ('23', '23'), ('24', '24'), ('25', '25'), ('26', '26'), ('27', '27'), ('28', '28'), ('29', '29'), ('30', '30'), ('31', '31'), ('67', '67'), ('68', '68'), ('69', '69'), ('39', '39'), ('39A', '39A'), ('40', '40'), ('41', '41'), ('42', '42'), ('43', '43'), ('44', '44'), ('45', '45'), ('46', '46'), ('47', '47'), ('48', '48'), ('49', '49'), ('50', '50'), ('51', '51'), ('66', '66')], max_length=10, verbose_name='POS'),
        ),
        migrations.AlterField(
            model_name='pintura',
            name='sector',
            field=models.CharField(choices=[('PLAT. COMERCIAL', 'PLAT. COMERCIAL'), ('PLAT. INDUSTRIAL', 'PLAT. INDUSTRIAL'), ('PLAT. SUR', 'PLAT. SUR')], max_length=50, verbose_name='Sector'),
        ),
    ]
