# Generated by Django 4.1.3 on 2023-04-17 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DERRAMES', '0003_alter_derrame_juntas_alter_derrame_pintura_afectada'),
    ]

    operations = [
        migrations.AlterField(
            model_name='derrame',
            name='estado',
            field=models.CharField(choices=[('ABIERTO', 'ABIERTO'), ('CERRADO', 'CERRADO')], default='ABIERTO', max_length=20, verbose_name='Estado'),
        ),
    ]
