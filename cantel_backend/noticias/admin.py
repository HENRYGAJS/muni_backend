from django.contrib import admin
from .models import Noticia, Evento, ReporteCiudadano
from django.urls import reverse
from django.utils.html import format_html
from django.contrib.admin import AdminSite
from django.urls import path
from django.shortcuts import render
from django.db import models
from .models import LugarTuristico, ImagenTuristica
from .models import EventoCultural, ImagenCultural
from .models import PlatoGastronomico, ImagenGastronomica
from .models import LugarHospedaje, ImagenHospedaje
from .models import Gasolinera, ImagenGasolinera
from .models import Tramite, ImagenTramite, ArchivoTramite
from .models import Servicio, ImagenServicio, ArchivoServicio
from .models import Noticia, ImagenNoticia
from .models import Evento, ImagenEvento

from .models import CorporacionActual, ImagenCorporacion

from .models import HistoriaCantel, ImagenHistoriaCantel




from .models import Inicio, ImagenPalacioMunicipal, ImagenEscudoMunicipal

class ImagenPalacioMunicipalInline(admin.TabularInline):
    model = ImagenPalacioMunicipal
    extra = 1

class ImagenEscudoMunicipalInline(admin.TabularInline):
    model = ImagenEscudoMunicipal
    extra = 1

@admin.register(Inicio)
class InicioAdmin(admin.ModelAdmin):
    inlines = [ImagenPalacioMunicipalInline, ImagenEscudoMunicipalInline]
    list_display = ('eslogan', 'administracion')
    search_fields = ('eslogan', 'administracion')






# Registro de Noticia y Evento


class ImagenNoticiaInline(admin.TabularInline):
    model = ImagenNoticia
    extra = 1  # Permitir agregar más de una imagen

@admin.register(Noticia)
class NoticiaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'fecha_creacion')
    inlines = [ImagenNoticiaInline]






class ImagenEventoInline(admin.TabularInline):
    model = ImagenEvento
    extra = 1  # Permitir subir más de una imagen

@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'fecha_evento', 'fecha_creacion')
    inlines = [ImagenEventoInline]





class ImagenCorporacionInline(admin.TabularInline):
    model = ImagenCorporacion
    extra = 1  # Permitir subir más de una imagen

@admin.register(CorporacionActual)
class CorporacionActualAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'fecha_creacion')
    inlines = [ImagenCorporacionInline]





class ImagenHistoriaCantelInline(admin.TabularInline):
    model = ImagenHistoriaCantel
    extra = 1  # Permitir subir más de una imagen

@admin.register(HistoriaCantel)
class HistoriaCantelAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'fecha_creacion')
    inlines = [ImagenHistoriaCantelInline]



class ImagenTuristicaInline(admin.TabularInline):
    model = ImagenTuristica
    extra = 1  # Permitir agregar más imágenes desde el administrador

@admin.register(LugarTuristico)
class LugarTuristicoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'fecha_creacion')
    inlines = [ImagenTuristicaInline]




class ImagenCulturalInline(admin.TabularInline):
    model = ImagenCultural
    extra = 1  # Permitir agregar múltiples imágenes desde el administrador

@admin.register(EventoCultural)
class EventoCulturalAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'fecha_creacion')
    inlines = [ImagenCulturalInline]






class ImagenGastronomicaInline(admin.TabularInline):
    model = ImagenGastronomica
    extra = 1  # Permitir agregar múltiples imágenes desde el administrador

@admin.register(PlatoGastronomico)
class PlatoGastronomicoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'fecha_creacion')
    inlines = [ImagenGastronomicaInline]





class ImagenHospedajeInline(admin.TabularInline):
    model = ImagenHospedaje
    extra = 1  # Permitir agregar múltiples imágenes desde el administrador

@admin.register(LugarHospedaje)
class LugarHospedajeAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'fecha_creacion')
    inlines = [ImagenHospedajeInline]






class ImagenGasolineraInline(admin.TabularInline):
    model = ImagenGasolinera
    extra = 1  # Permite agregar una imagen adicional por defecto

@admin.register(Gasolinera)
class GasolineraAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'direccion', 'fecha_creacion')
    search_fields = ('nombre', 'direccion')
    inlines = [ImagenGasolineraInline]


# Registrar el modelo ReporteCiudadano solo una vez
@admin.register(ReporteCiudadano)
class ReporteCiudadanoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'asunto', 'correo', 'telefono', 'fecha_reporte', 'descargar_pdf')
    search_fields = ('nombre', 'correo', 'telefono', 'asunto')
    list_filter = ('asunto', 'fecha_reporte')

    # Función para descargar el PDF
    def descargar_pdf(self, obj):
        url = reverse('generar_pdf_reporte', args=[obj.id])
        return format_html('<a href="{}">Descargar PDF</a>', url)

    descargar_pdf.short_description = 'Orden de Trabajo'

# Personalización del sitio de administración
class MiAdminSite(AdminSite):
    site_header = "Administración de Reportes Ciudadanos"
    site_title = "Panel de Administración"
    index_title = "Estadísticas de Reportes"

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('estadisticas/', self.admin_view(self.estadisticas), name="estadisticas"),
        ]
        return custom_urls + urls

    def estadisticas(self, request):
        total_reportes = ReporteCiudadano.objects.count()
        reportes_por_asunto = ReporteCiudadano.objects.values('asunto').annotate(total=models.Count('asunto'))

        context = dict(
            self.each_context(request),
            total_reportes=total_reportes,
            reportes_por_asunto=reportes_por_asunto,
        )
        return render(request, 'admin/estadisticas.html', context)

# Utiliza MiAdminSite para manejar la administración
admin_site = MiAdminSite(name='admin')




class ImagenTramiteInline(admin.TabularInline):
    model = ImagenTramite
    extra = 1

class ArchivoTramiteInline(admin.TabularInline):
    model = ArchivoTramite
    extra = 1

@admin.register(Tramite)
class TramiteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'fecha_creacion')
    inlines = [ImagenTramiteInline, ArchivoTramiteInline]





class ImagenServicioInline(admin.TabularInline):
    model = ImagenServicio
    extra = 1

class ArchivoServicioInline(admin.TabularInline):
    model = ArchivoServicio
    extra = 1

@admin.register(Servicio)
class ServicioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'fecha_creacion')
    inlines = [ImagenServicioInline, ArchivoServicioInline]