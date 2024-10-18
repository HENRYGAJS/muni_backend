# Generated by Django 5.1.1 on 2024-10-04 15:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noticias', '0016_historiacantel_imagenhistoriacantel'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eslogan', models.CharField(max_length=255)),
                ('administracion', models.CharField(max_length=255)),
                ('descripcion', models.TextField()),
                ('imagen_edificio_municipal', models.ImageField(upload_to='edificio_municipal/')),
                ('imagen_escudo_municipal', models.ImageField(upload_to='escudo_municipal/')),
            ],
        ),
        migrations.CreateModel(
            name='ImagenEdificioMunicipal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(upload_to='edificio_municipal/')),
                ('inicio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='imagenes_edificio', to='noticias.inicio')),
            ],
        ),
    ]
