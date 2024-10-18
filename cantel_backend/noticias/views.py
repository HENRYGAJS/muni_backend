from django.shortcuts import render
from .models import Noticia
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Noticia
from .models import Evento
from .serializers import NoticiaSerializer
from .serializers import EventoSerializer
from rest_framework import status
from .serializers import ReporteCiudadanoSerializer



from .models import CorporacionActual
from .serializers import CorporacionActualSerializer


from .models import LugarTuristico
from .serializers import LugarTuristicoSerializer


from .models import EventoCultural
from .serializers import EventoCulturalSerializer

from .models import PlatoGastronomico
from .serializers import PlatoGastronomicoSerializer


from .models import LugarHospedaje
from .serializers import LugarHospedajeSerializer



from .models import Gasolinera
from .serializers import GasolineraSerializer


from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from .models import ReporteCiudadano


from .models import Tramite
from .serializers import TramiteSerializer

from .models import Servicio
from .serializers import ServicioSerializer

from .models import Noticia
from .serializers import NoticiaSerializer




from .models import CorporacionActual
from .serializers import CorporacionActualSerializer


from .models import HistoriaCantel
from .serializers import HistoriaCantelSerializer

from .models import HistoriaCantel
from .serializers import HistoriaCantelSerializer


from .models import Inicio
from .serializers import InicioSerializer

@api_view(['GET'])
def obtener_inicio(request):
    inicio = Inicio.objects.first()  # Obtenemos el primer registro
    serializer = InicioSerializer(inicio)
    return Response(serializer.data)









@api_view(['GET'])
def lista_noticias(request):
    noticias = Noticia.objects.all()
    serializer = NoticiaSerializer(noticias, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def api_lista_noticias_recientes(request):
    noticias = Noticia.objects.all().order_by('-fecha_creacion')[:3]  # Limitamos a las 3 más recientes
    serializer = NoticiaSerializer(noticias, many=True)
    return Response(serializer.data)






@api_view(['GET'])
def api_lista_todas_noticias(request):
    noticias = Noticia.objects.all().order_by('-fecha_creacion')
    serializer = NoticiaSerializer(noticias, many=True)
    return Response(serializer.data)




@api_view(['GET'])
def api_lista_eventos(request):
    eventos = Evento.objects.all().order_by('-fecha_creacion')
    serializer = EventoSerializer(eventos, many=True)
    return Response(serializer.data)








@api_view(['GET'])
def obtener_corporacion_actual(request):
    try:
        corporacion = CorporacionActual.objects.latest('fecha_creacion')  # Obtener la última corporación creada
        serializer = CorporacionActualSerializer(corporacion)
        return Response(serializer.data)
    except CorporacionActual.DoesNotExist:
        return Response({'error': 'No se ha encontrado ninguna corporación actual.'}, status=404)






@api_view(['GET'])
def obtener_historias_cantel(request):
    historias = HistoriaCantel.objects.all()  # Obtener todas las historias
    serializer = HistoriaCantelSerializer(historias, many=True)  # many=True porque es una lista
    return Response(serializer.data)





@api_view(['GET'])
def lista_lugares_turisticos(request):
    lugares = LugarTuristico.objects.all()
    serializer = LugarTuristicoSerializer(lugares, many=True)
    return Response(serializer.data)






@api_view(['GET'])
def lista_eventos_culturales(request):
    eventos = EventoCultural.objects.all()
    serializer = EventoCulturalSerializer(eventos, many=True)
    return Response(serializer.data)







@api_view(['GET'])
def lista_platos_gastronomicos(request):
    platos = PlatoGastronomico.objects.all()
    serializer = PlatoGastronomicoSerializer(platos, many=True)
    return Response(serializer.data)







@api_view(['GET'])
def lista_lugares_hospedaje(request):
    lugares = LugarHospedaje.objects.all()
    serializer = LugarHospedajeSerializer(lugares, many=True)
    return Response(serializer.data)





@api_view(['GET'])
def lista_gasolineras(request):
    gasolineras = Gasolinera.objects.all()
    serializer = GasolineraSerializer(gasolineras, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def crear_reporte_ciudadano(request):
    if request.method == 'POST':
        serializer = ReporteCiudadanoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



def generar_pdf_reporte(request, reporte_id):
    # Obtener el reporte de la base de datos
    reporte = ReporteCiudadano.objects.get(id=reporte_id)

    # Cargar el template y renderizarlo con los datos del reporte
    template = get_template('pdf_template_reporte.html')
    context = {'reporte': reporte}
    html = template.render(context)

    # Crear el PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="orden_trabajo_{reporte.id}.pdf"'
    pisa_status = pisa.CreatePDF(html, dest=response)

    if pisa_status.err:
        return HttpResponse('Hubo un error al generar el PDF', status=400)
    
    return response




@api_view(['GET'])
def lista_tramites(request):
    tramites = Tramite.objects.all()
    serializer = TramiteSerializer(tramites, many=True)
    return Response(serializer.data)




@api_view(['GET'])
def lista_servicios(request):
    servicios = Servicio.objects.all()
    serializer = ServicioSerializer(servicios, many=True)
    return Response(serializer.data)