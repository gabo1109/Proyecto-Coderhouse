# Generated by Django 4.2.2 on 2023-06-26 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inicio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gato',
            name='fecha_nacimiento',
            field=models.DateField(null=True),
        ),
    ]
