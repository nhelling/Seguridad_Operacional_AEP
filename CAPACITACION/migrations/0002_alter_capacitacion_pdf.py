# Generated by Django 4.1.3 on 2023-04-24 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CAPACITACION', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='capacitacion',
            name='pdf',
            field=models.FileField(blank=True, null=True, upload_to='pdf'),
        ),
    ]
