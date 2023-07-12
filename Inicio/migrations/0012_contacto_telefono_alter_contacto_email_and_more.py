# Generated by Django 4.2.2 on 2023-06-29 15:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Inicio', '0011_contacto'),
    ]

    operations = [
        migrations.AddField(
            model_name='contacto',
            name='telefono',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contacto',
            name='email',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='contacto',
            name='mensaje',
            field=models.CharField(max_length=1000),
        ),
    ]