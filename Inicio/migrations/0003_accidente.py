# Generated by Django 4.2.2 on 2023-06-27 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inicio', '0002_alter_gato_fecha_nacimiento'),
    ]

    operations = [
        migrations.CreateModel(
            name='Accidente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('crashid', models.IntegerField()),
                ('fecha', models.DateField(null=True)),
                ('location', models.CharField(max_length=100)),
                ('modelo', models.CharField(max_length=100)),
            ],
        ),
    ]