# Generated by Django 4.2.2 on 2023-06-27 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inicio', '0007_informe_causa_accidente_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='informe',
            name='causa_accidente',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='informe',
            name='descripcion_accidente',
            field=models.CharField(max_length=1000),
        ),
    ]
