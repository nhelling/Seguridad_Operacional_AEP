# Generated by Django 4.1.3 on 2023-04-24 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PNSO', '0007_alter_pnso_cierre_alter_pnso_estado_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pnso',
            name='image_pnso',
            field=models.ImageField(blank=True, null=True, upload_to='image_pnso'),
        ),
    ]
