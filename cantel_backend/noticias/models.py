from django.db import models





class Inicio(models.Model):
    eslogan = models.CharField(max_length=255)
    administracion = models.CharField(max_length=255)
    descripcion = models.TextField()

class ImagenPalacioMunicipal(models.Model):
    inicio = models.ForeignKey(Inicio, related_name='imagenes_palacio', on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='palacio_municipal/')

class ImagenEscudoMunicipal(models.Model):
    inicio = models.ForeignKey(Inicio, related_name='imagenes_escudo', on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='escudo_municipal/')




class Noticia(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()  # Campo para la descripción
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

class ImagenNoticia(models.Model):
    noticia = models.ForeignKey(Noticia, related_name='imagenes', on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='noticias/imagenes/')
    
    def __str__(self):
        return f"Imagen de {self.noticia.titulo}"



class Evento(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha_evento = models.DateField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

class ImagenEvento(models.Model):
    evento = models.ForeignKey(Evento, related_name='imagenes', on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='eventos/imagenes/')

    def __str__(self):
        return f"Imagen de {self.evento.titulo}"





class CorporacionActual(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    mision = models.TextField()
    vision = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Corporación Actual'
        verbose_name_plural = 'Corporación Actual'

    def __str__(self):
        return self.titulo

class ImagenCorporacion(models.Model):
    corporacion = models.ForeignKey(CorporacionActual, related_name='imagenes', on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='corporacion/imagenes/')

    def __str__(self):
        return f"Imagen de {self.corporacion.titulo}"




class HistoriaCantel(models.Model):
    titulo = models.CharField(max_length=200)
    subtitulo = models.CharField(max_length=300)
    descripcion = models.TextField(max_length=2000)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Historia de Cantel'
        verbose_name_plural = 'Historia de Cantel'

    def __str__(self):
        return self.titulo

class ImagenHistoriaCantel(models.Model):
    historia = models.ForeignKey(HistoriaCantel, related_name='imagenes', on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='historia_cantel/imagenes/')

    def __str__(self):
        return f"Imagen de {self.historia.titulo}"






class LugarTuristico(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre

class ImagenTuristica(models.Model):
    lugar = models.ForeignKey(LugarTuristico, related_name='imagenes', on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='turismo/imagenes/')
    
    def __str__(self):
        return f"Imagen de {self.lugar.nombre}"
    


class EventoCultural(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre

class ImagenCultural(models.Model):
    evento = models.ForeignKey(EventoCultural, related_name='imagenes', on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='cultura/imagenes/')
    
    def __str__(self):
        return f"Imagen de {self.evento.nombre}"




class PlatoGastronomico(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre

class ImagenGastronomica(models.Model):
    plato = models.ForeignKey(PlatoGastronomico, related_name='imagenes', on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='gastronomia/imagenes/')
    
    def __str__(self):
        return f"Imagen de {self.plato.nombre}"





class LugarHospedaje(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre

class ImagenHospedaje(models.Model):
    lugar = models.ForeignKey(LugarHospedaje, related_name='imagenes', on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='hospedaje/imagenes/')
    
    def __str__(self):
        return f"Imagen de {self.lugar.nombre}"




class Gasolinera(models.Model):
    nombre = models.CharField(max_length=200)
    direccion = models.CharField(max_length=300)
    descripcion = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre

class ImagenGasolinera(models.Model):
    gasolinera = models.ForeignKey(Gasolinera, related_name='imagenes', on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='gasolineras/imagenes/')

    def __str__(self):
        return f"Imagen de {self.gasolinera.nombre}"




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

    def __str__(self):
        return f"{self.nombre} - {self.asunto}"





class Tramite(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre

class ImagenTramite(models.Model):
    tramite = models.ForeignKey(Tramite, related_name='imagenes', on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='tramites/imagenes/')
    
    def __str__(self):
        return f"Imagen de {self.tramite.nombre}"

class ArchivoTramite(models.Model):
    tramite = models.ForeignKey(Tramite, related_name='archivos', on_delete=models.CASCADE)
    archivo = models.FileField(upload_to='tramites/archivos/')
    
    def __str__(self):
        return f"Archivo de {self.tramite.nombre}"




class Servicio(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre

class ImagenServicio(models.Model):
    servicio = models.ForeignKey(Servicio, related_name='imagenes', on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='servicios/imagenes/')
    
    def __str__(self):
        return f"Imagen de {self.servicio.nombre}"

class ArchivoServicio(models.Model):
    servicio = models.ForeignKey(Servicio, related_name='archivos', on_delete=models.CASCADE)
    archivo = models.FileField(upload_to='servicios/archivos/')
    
    def __str__(self):
        return f"Archivo de {self.servicio.nombre}"