
from django.urls import path
from . import views
from .views import crear_reporte_ciudadano
from .views import generar_pdf_reporte
from .views import lista_lugares_turisticos
from .views import lista_eventos_culturales
from .views import lista_platos_gastronomicos
from .views import lista_lugares_hospedaje
from .views import lista_gasolineras
from .views import lista_tramites
from .views import lista_servicios
from .views import obtener_corporacion_actual
from .views import obtener_historias_cantel
from .views import obtener_inicio

urlpatterns = [
    path('api/noticias_recientes/', views.api_lista_noticias_recientes, name='api_lista_noticias_recientes'),
    path('api/todas_noticias/', views.api_lista_todas_noticias, name='api_lista_todas_noticias'),
    path('api/eventos/', views.api_lista_eventos, name='api_lista_eventos'),
    path('api/crear_reporte/', crear_reporte_ciudadano, name='crear_reporte_ciudadano'),
    path('reporte/pdf/<int:reporte_id>/', generar_pdf_reporte, name='generar_pdf_reporte'),
    path('api/lugares_turisticos/', lista_lugares_turisticos, name='lista_lugares_turisticos'),
    path('api/eventos_culturales/', lista_eventos_culturales, name='lista_eventos_culturales'),
    path('api/platos_gastronomicos/', lista_platos_gastronomicos, name='lista_platos_gastronomicos'),
    path('api/lugares_hospedaje/', lista_lugares_hospedaje, name='lista_lugares_hospedaje'),
    path('api/gasolineras/', lista_gasolineras, name='lista_gasolineras'),
    path('api/tramites/', lista_tramites, name='lista_tramites'),
    path('api/servicios/', lista_servicios, name='lista_servicios'),
    path('api/corporacion_actual/', obtener_corporacion_actual, name='obtener_corporacion_actual'),
    path('api/historia_cantel/', obtener_historias_cantel, name='obtener_historia_cantel'),
    path('api/inicio/', obtener_inicio, name='obtener_inicio'),
    
    
    
]

