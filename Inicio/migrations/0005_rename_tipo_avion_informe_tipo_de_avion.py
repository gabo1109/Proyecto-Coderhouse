# Generated by Django 4.2.2 on 2023-06-27 23:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Inicio', '0004_informe_delete_gato'),
    ]

    operations = [
        migrations.RenameField(
            model_name='informe',
            old_name='tipo_avion',
            new_name='tipo_de_avion',
        ),
    ]
