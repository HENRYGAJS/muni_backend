from rest_framework import serializers
from .models import Noticia
from .models import Evento
from .models import ReporteCiudadano









from .models import Inicio, ImagenPalacioMunicipal, ImagenEscudoMunicipal

class ImagenPalacioMunicipalSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImagenPalacioMunicipal
        fields = ['imagen']

class ImagenEscudoMunicipalSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImagenEscudoMunicipal
        fields = ['imagen']

class InicioSerializer(serializers.ModelSerializer):
    imagenes_palacio = ImagenPalacioMunicipalSerializer(many=True)
    imagenes_escudo = ImagenEscudoMunicipalSerializer(many=True)

    class Meta:
        model = Inicio
        fields = ['eslogan', 'administracion', 'descripcion', 'imagenes_palacio', 'imagenes_escudo']















from .models import Noticia, ImagenNoticia

class ImagenNoticiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImagenNoticia
        fields = ['imagen']

class NoticiaSerializer(serializers.ModelSerializer):
    imagenes = ImagenNoticiaSerializer(many=True, read_only=True)

    class Meta:
        model = Noticia
        fields = ['id', 'titulo', 'descripcion', 'imagenes']  # Incluir el campo descripcion




from .models import Evento, ImagenEvento

class ImagenEventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImagenEvento
        fields = ['imagen']

class EventoSerializer(serializers.ModelSerializer):
    imagenes = ImagenEventoSerializer(many=True, read_only=True)

    class Meta:
        model = Evento
        fields = ['id', 'titulo', 'descripcion', 'fecha_evento', 'imagenes']





from .models import CorporacionActual, ImagenCorporacion

class ImagenCorporacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImagenCorporacion
        fields = ['imagen']

class CorporacionActualSerializer(serializers.ModelSerializer):
    imagenes = ImagenCorporacionSerializer(many=True, read_only=True)

    class Meta:
        model = CorporacionActual
        fields = ['id', 'titulo', 'descripcion', 'mision', 'vision', 'imagenes']





from .models import HistoriaCantel, ImagenHistoriaCantel

class ImagenHistoriaCantelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImagenHistoriaCantel
        fields = ['imagen']

class HistoriaCantelSerializer(serializers.ModelSerializer):
    imagenes = ImagenHistoriaCantelSerializer(many=True, read_only=True)

    class Meta:
        model = HistoriaCantel
        fields = ['id', 'titulo', 'subtitulo', 'descripcion', 'imagenes']




from .models import LugarTuristico, ImagenTuristica

class ImagenTuristicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImagenTuristica
        fields = ['imagen']

class LugarTuristicoSerializer(serializers.ModelSerializer):
    imagenes = ImagenTuristicaSerializer(many=True, read_only=True)

    class Meta:
        model = LugarTuristico
        fields = ['id', 'nombre', 'descripcion', 'fecha_creacion', 'imagenes']




from .models import EventoCultural, ImagenCultural

class ImagenCulturalSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImagenCultural
        fields = ['imagen']

class EventoCulturalSerializer(serializers.ModelSerializer):
    imagenes = ImagenCulturalSerializer(many=True, read_only=True)

    class Meta:
        model = EventoCultural
        fields = ['id', 'nombre', 'descripcion', 'fecha_creacion', 'imagenes']



from .models import PlatoGastronomico, ImagenGastronomica

class ImagenGastronomicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImagenGastronomica
        fields = ['imagen']

class PlatoGastronomicoSerializer(serializers.ModelSerializer):
    imagenes = ImagenGastronomicaSerializer(many=True, read_only=True)

    class Meta:
        model = PlatoGastronomico
        fields = ['id', 'nombre', 'descripcion', 'fecha_creacion', 'imagenes']






from .models import LugarHospedaje, ImagenHospedaje

class ImagenHospedajeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImagenHospedaje
        fields = ['imagen']

class LugarHospedajeSerializer(serializers.ModelSerializer):
    imagenes = ImagenHospedajeSerializer(many=True, read_only=True)

    class Meta:
        model = LugarHospedaje
        fields = ['id', 'nombre', 'descripcion', 'fecha_creacion', 'imagenes']




from .models import Gasolinera, ImagenGasolinera

class ImagenGasolineraSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImagenGasolinera
        fields = ['imagen']

class GasolineraSerializer(serializers.ModelSerializer):
    imagenes = ImagenGasolineraSerializer(many=True, read_only=True)

    class Meta:
        model = Gasolinera
        fields = ['id', 'nombre', 'direccion', 'descripcion', 'fecha_creacion', 'imagenes']





class ReporteCiudadanoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReporteCiudadano
        fields = ['id', 'nombre', 'correo', 'telefono', 'asunto', 'mensaje', 'enlace_ubicacion', 'latitud', 'longitud', 'fecha_reporte']





from .models import Tramite, ImagenTramite, ArchivoTramite

class ImagenTramiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImagenTramite
        fields = ['imagen']

class ArchivoTramiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArchivoTramite
        fields = ['archivo']

class TramiteSerializer(serializers.ModelSerializer):
    imagenes = ImagenTramiteSerializer(many=True, read_only=True)
    archivos = ArchivoTramiteSerializer(many=True, read_only=True)

    class Meta:
        model = Tramite
        fields = ['id', 'nombre', 'descripcion', 'fecha_creacion', 'imagenes', 'archivos']




from .models import Servicio, ImagenServicio, ArchivoServicio

class ImagenServicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImagenServicio
        fields = ['imagen']

class ArchivoServicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArchivoServicio
        fields = ['archivo']

class ServicioSerializer(serializers.ModelSerializer):
    imagenes = ImagenServicioSerializer(many=True, read_only=True)
    archivos = ArchivoServicioSerializer(many=True, read_only=True)

    class Meta:
        model = Servicio
        fields = ['id', 'nombre', 'descripcion', 'fecha_creacion', 'imagenes', 'archivos']