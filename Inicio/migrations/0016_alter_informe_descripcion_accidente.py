# Generated by Django 4.2.2 on 2023-08-07 18:32

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Inicio', '0015_alter_contacto_telefono'),
    ]

    operations = [
        migrations.AlterField(
            model_name='informe',
            name='descripcion_accidente',
            field=ckeditor.fields.RichTextField(null=True),
        ),
    ]
