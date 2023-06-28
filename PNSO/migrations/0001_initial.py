# Generated by Django 4.1.7 on 2023-02-18 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fleet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nro', models.IntegerField(verbose_name='ID')),
                ('fecha_recibido', models.DateField(verbose_name='Fecha Recibido')),
                ('fecha_evento', models.DateField(verbose_name='Fecha Evento')),
                ('texto', models.CharField(max_length=3000, verbose_name='Texto')),
                ('fecha_respuesta', models.CharField(max_length=3000, verbose_name='Fecha Respuesta')),
                ('estado', models.CharField(max_length=1, verbose_name='Estado')),
                ('mitigacion', models.CharField(max_length=3000, verbose_name='Mitigacion')),
                ('cierre', models.CharField(max_length=10, verbose_name='Cierre')),
            ],
            options={
                'verbose_name': 'PNSO',
                'verbose_name_plural': 'PNSOs',
            },
        ),
    ]
