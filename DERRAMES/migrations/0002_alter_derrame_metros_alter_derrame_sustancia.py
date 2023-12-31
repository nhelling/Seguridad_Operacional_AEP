# Generated by Django 4.1.7 on 2023-04-07 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DERRAMES', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='derrame',
            name='metros',
            field=models.CharField(max_length=5, verbose_name='m2'),
        ),
        migrations.AlterField(
            model_name='derrame',
            name='sustancia',
            field=models.CharField(choices=[('COMBUSTIBLE AERONAUTICO', 'COMBUSTIBLE AERONAUTICO'), ('COMBUSTIBLE TERRESTRE', 'COMBUSTIBLE TERRESTRE'), ('LIQUIDO HIDRAULICO', 'LIQUIDO HIDRAULICO'), ('ACEITES TERRESTRES', 'ACEITES TERRESTRES'), ('ACEITES AERONAUTICOS', 'ACEITES AERONAUTICOS'), ('OTROS', 'OTROS')], max_length=100, verbose_name='Sustancia'),
        ),
    ]
