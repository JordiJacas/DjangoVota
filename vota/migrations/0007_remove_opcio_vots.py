# Generated by Django 2.0.1 on 2018-02-01 16:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vota', '0006_remove_opcio_usuari'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='opcio',
            name='vots',
        ),
    ]
