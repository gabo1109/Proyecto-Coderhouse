# Generated by Django 4.2.2 on 2023-06-27 23:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Inicio', '0005_rename_tipo_avion_informe_tipo_de_avion'),
    ]

    operations = [
        migrations.RenameField(
            model_name='informe',
            old_name='tipo_de_avion',
            new_name='tipo_avion',
        ),
    ]
