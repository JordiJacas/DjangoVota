# Generated by Django 2.0.1 on 2018-02-01 16:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vota', '0007_remove_opcio_vots'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vot',
            old_name='Opcio',
            new_name='opcio',
        ),
    ]
