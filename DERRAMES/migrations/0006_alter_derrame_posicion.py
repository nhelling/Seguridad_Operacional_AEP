# Generated by Django 4.1.7 on 2023-05-01 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DERRAMES', '0005_alter_derrame_empresa_alter_derrame_sustancia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='derrame',
            name='posicion',
            field=models.CharField(choices=[('01', '01'), ('02', '02'), ('PAS-03', 'PAS-03'), ('PAS-03A', 'PAS-03A'), ('PAS-03C', 'PAS-03C'), ('PAS-04', 'PAS-04'), ('PAS-05', 'PAS-05'), ('PAS-06', 'PAS-06'), ('PAS-07', 'PAS-07'), ('PAS-08', 'PAS-08'), ('PAS-09', 'PAS-09'), ('PAS-10', 'PAS-10'), ('PAS-11', 'PAS-11'), ('PAS-12', 'PAS-12'), ('13', '13'), ('14', '14'), ('15', '15'), ('16', '16'), ('17', '17'), ('18', '18'), ('19', '19'), ('20', '20'), ('21', '21'), ('22', '22'), ('23', '23'), ('24', '24'), ('25', '25'), ('26', '26'), ('27', '27'), ('28', '28'), ('29', '29'), ('30', '30'), ('31', '31'), ('32A', '32A'), ('32B', '32B'), ('32C', '32C'), ('67', '67'), ('68', '68'), ('69', '69'), ('39', '39'), ('39A', '39A'), ('40', '40'), ('41', '41'), ('42', '42'), ('43', '43'), ('44', '44'), ('45', '45'), ('46', '46'), ('47', '47'), ('48', '48'), ('49', '49'), ('50', '50'), ('51', '51'), ('66', '66')], max_length=100, verbose_name='Posicion'),
        ),
    ]
