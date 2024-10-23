from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver
import os

# Función para eliminar archivos del sistema de archivos
#def eliminar_archivo(instance, **kwargs):
#    if hasattr(instance, 'imagen') and instance.imagen:
#        if os.path.isfile(instance.imagen.path):
#            os.remove(instance.imagen.path)
#    if hasattr(instance, 'archivo') and instance.archivo:
#        if os.path.isfile(instance.archivo.path):
#            os.remove(instance.archivo.path)




import boto3
from django.conf import settings

s3_client = boto3.client('s3', 
    aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
    aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
    region_name=settings.AWS_S3_REGION_NAME
)

def eliminar_archivo(instance, **kwargs):
    if hasattr(instance, 'imagen') and instance.imagen:
        try:
            s3_client.delete_object(Bucket=settings.AWS_STORAGE_BUCKET_NAME, Key=instance.imagen.name)
        except Exception as e:
            print(f"Error al eliminar el archivo {instance.imagen.name}: {e}")
    if hasattr(instance, 'archivo') and instance.archivo:
        try:
            s3_client.delete_object(Bucket=settings.AWS_STORAGE_BUCKET_NAME, Key=instance.archivo.name)
        except Exception as e:
            print(f"Error al eliminar el archivo {instance.archivo.name}: {e}")



# Modelos con señales

# Inicio
class Inicio(models.Model):
    eslogan = models.CharField(max_length=255)
    administracion = models.CharField(max_length=255)
    descripcion = models.TextField()

class ImagenPalacioMunicipal(models.Model):
    inicio = models.ForeignKey(Inicio, related_name='imagenes_palacio', on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='palacio_municipal/')

@receiver(post_delete, sender=ImagenPalacioMunicipal)
def eliminar_imagen_palacio(sender, instance, **kwargs):
    eliminar_archivo(instance)

class ImagenEscudoMunicipal(models.Model):
    inicio = models.ForeignKey(Inicio, related_name='imagenes_escudo', on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='escudo_municipal/')

@receiver(post_delete, sender=ImagenEscudoMunicipal)
def eliminar_imagen_escudo(sender, instance, **kwargs):
    eliminar_archivo(instance)

# Noticias
class Noticia(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

class ImagenNoticia(models.Model):
    noticia = models.ForeignKey(Noticia, related_name='imagenes', on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='noticias/imagenes/')

@receiver(post_delete, sender=ImagenNoticia)
def eliminar_imagen_noticia(sender, instance, **kwargs):
    eliminar_archivo(instance)

# Eventos
class Evento(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha_evento = models.DateField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

class ImagenEvento(models.Model):
    evento = models.ForeignKey(Evento, related_name='imagenes', on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='eventos/imagenes/')

@receiver(post_delete, sender=ImagenEvento)
def eliminar_imagen_evento(sender, instance, **kwargs):
    eliminar_archivo(instance)

# Corporación Actual
class CorporacionActual(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    mision = models.TextField()
    vision = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

class ImagenCorporacion(models.Model):
    corporacion = models.ForeignKey(CorporacionActual, related_name='imagenes', on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='corporacion/imagenes/')

@receiver(post_delete, sender=ImagenCorporacion)
def eliminar_imagen_corporacion(sender, instance, **kwargs):
    eliminar_archivo(instance)

# Historia Cantel
class HistoriaCantel(models.Model):
    titulo = models.CharField(max_length=200)
    subtitulo = models.CharField(max_length=300)
    descripcion = models.TextField(max_length=2000)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

class ImagenHistoriaCantel(models.Model):
    historia = models.ForeignKey(HistoriaCantel, related_name='imagenes', on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='historia_cantel/imagenes/')

@receiver(post_delete, sender=ImagenHistoriaCantel)
def eliminar_imagen_historia(sender, instance, **kwargs):
    eliminar_archivo(instance)

# Lugar Turístico
class LugarTuristico(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

class ImagenTuristica(models.Model):
    lugar = models.ForeignKey(LugarTuristico, related_name='imagenes', on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='turismo/imagenes/')

@receiver(post_delete, sender=ImagenTuristica)
def eliminar_imagen_turistica(sender, instance, **kwargs):
    eliminar_archivo(instance)

# Evento Cultural
class EventoCultural(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

class ImagenCultural(models.Model):
    evento = models.ForeignKey(EventoCultural, related_name='imagenes', on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='cultura/imagenes/')

@receiver(post_delete, sender=ImagenCultural)
def eliminar_imagen_cultural(sender, instance, **kwargs):
    eliminar_archivo(instance)

# Plato Gastronómico
class PlatoGastronomico(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

class ImagenGastronomica(models.Model):
    plato = models.ForeignKey(PlatoGastronomico, related_name='imagenes', on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='gastronomia/imagenes/')

@receiver(post_delete, sender=ImagenGastronomica)
def eliminar_imagen_gastronomia(sender, instance, **kwargs):
    eliminar_archivo(instance)

# Lugar Hospedaje
class LugarHospedaje(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

class ImagenHospedaje(models.Model):
    lugar = models.ForeignKey(LugarHospedaje, related_name='imagenes', on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='hospedaje/imagenes/')

@receiver(post_delete, sender=ImagenHospedaje)
def eliminar_imagen_hospedaje(sender, instance, **kwargs):
    eliminar_archivo(instance)

# Gasolineras
class Gasolinera(models.Model):
    nombre = models.CharField(max_length=200)
    direccion = models.CharField(max_length=300)
    descripcion = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

class ImagenGasolinera(models.Model):
    gasolinera = models.ForeignKey(Gasolinera, related_name='imagenes', on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='gasolineras/imagenes/')

@receiver(post_delete, sender=ImagenGasolinera)
def eliminar_imagen_gasolinera(sender, instance, **kwargs):
    eliminar_archivo(instance)

# Reporte Ciudadano
class ReporteCiudadano(models.Model):
    ASUNTO_CHOICES = [
        ('calle', 'Calle en mal estado'),
        ('alumbrado', 'Alumbrado público'),
        ('drenaje', 'Daño a drenaje'),
        ('tuberia', 'Daño a tubería de agua'),
        ('otros', 'Otros'),
    ]
    nombre = models.CharField(max_length=100)
    correo = models.EmailField()
    telefono = models.CharField(max_length=15)
    asunto = models.CharField(max_length=50, choices=ASUNTO_CHOICES)
    mensaje = models.TextField()
    enlace_ubicacion = models.URLField()
    fecha_reporte = models.DateTimeField(auto_now_add=True)
    latitud = models.FloatField()
    longitud = models.FloatField()

# Trámites
class Tramite(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

class ImagenTramite(models.Model):
    tramite = models.ForeignKey(Tramite, related_name='imagenes', on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='tramites/imagenes/')

@receiver(post_delete, sender=ImagenTramite)
def eliminar_imagen_tramite(sender, instance, **kwargs):
    eliminar_archivo(instance)

class ArchivoTramite(models.Model):
    tramite = models.ForeignKey(Tramite, related_name='archivos', on_delete=models.CASCADE)
    archivo = models.FileField(upload_to='tramites/archivos/')

@receiver(post_delete, sender=ArchivoTramite)
def eliminar_archivo_tramite(sender, instance, **kwargs):
    eliminar_archivo(instance)

# Servicios
class Servicio(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

class ImagenServicio(models.Model):
    servicio = models.ForeignKey(Servicio, related_name='imagenes', on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='servicios/imagenes/')

@receiver(post_delete, sender=ImagenServicio)
def eliminar_imagen_servicio(sender, instance, **kwargs):
    eliminar_archivo(instance)

class ArchivoServicio(models.Model):
    servicio = models.ForeignKey(Servicio, related_name='archivos', on_delete=models.CASCADE)
    archivo = models.FileField(upload_to='servicios/archivos/')

@receiver(post_delete, sender=ArchivoServicio)
def eliminar_archivo_servicio(sender, instance, **kwargs):
    eliminar_archivo(instance)
