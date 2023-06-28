# Generated by Django 4.1.3 on 2023-05-02 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mapa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mapa', models.CharField(max_length=1000, verbose_name='Mapa')),
            ],
            options={
                'verbose_name': 'MAPA',
                'verbose_name_plural': 'MAPAS',
            },
        ),
    ]
