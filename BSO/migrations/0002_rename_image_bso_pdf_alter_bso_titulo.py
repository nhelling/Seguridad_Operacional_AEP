# Generated by Django 4.1.7 on 2023-03-24 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BSO', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bso',
            old_name='image',
            new_name='pdf',
        ),
        migrations.AlterField(
            model_name='bso',
            name='titulo',
            field=models.CharField(max_length=1000, verbose_name='Titulo'),
        ),
    ]
