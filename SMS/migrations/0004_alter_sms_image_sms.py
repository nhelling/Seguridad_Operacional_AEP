# Generated by Django 4.1.7 on 2023-05-01 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SMS', '0003_alter_sms_image_sms'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sms',
            name='image_sms',
            field=models.FileField(blank=True, null=True, upload_to='image_sms', verbose_name='RELEVAMIENTO FOTOGRAFICO'),
        ),
    ]
