# Generated by Django 4.2.2 on 2023-06-28 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inicio', '0008_alter_informe_causa_accidente_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Accidente',
        ),
        migrations.AddField(
            model_name='informe',
            name='numero_caso',
            field=models.IntegerField(default=0),
        ),
    ]
