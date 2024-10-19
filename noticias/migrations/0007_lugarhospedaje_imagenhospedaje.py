# Generated by Django 5.1.1 on 2024-10-03 07:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noticias', '0006_platogastronomico_imagengastronomica'),
    ]

    operations = [
        migrations.CreateModel(
            name='LugarHospedaje',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('descripcion', models.TextField()),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ImagenHospedaje',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(upload_to='hospedaje/imagenes/')),
                ('lugar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='imagenes', to='noticias.lugarhospedaje')),
            ],
        ),
    ]