# Generated by Django 4.2.2 on 2023-08-07 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Usuario', '0002_infoextra_descripcion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='infoextra',
            name='descripcion',
        ),
        migrations.AddField(
            model_name='infoextra',
            name='legajo',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]
