from django.shortcuts import render

from . import models
from django.templatetags.static import static
from django.http import HttpResponse

datos_tarjetas = [
    {"titulo": "Mesa", "texto": "Mesa de roble nórdica.", "precio": "USD 499" ,"imagen": static('core/img/Mesa.webp')},
    {"titulo": "Cama", "texto": "Cama para tener dulces sueños", "precio": "USD2.999" , "imagen": static('core/img/Cama.webp')},
    {"titulo": "Sillón", "texto": "Sillón para disfrutar tu lectura a pleno", "precio": "USD1.999" , "imagen": static('core/img/Sillón.webp')},
    {"titulo": "Butaca", "texto": "Butacas para invitar amigos", "precio": "USD199" , "imagen": static('core/img/Banqueta.webp')}]

def home(request):
    
    return render(request, "core/index.html", {"datos_tarjetas":datos_tarjetas})

def detalle_producto(request,title):
    datos = [item for item in datos_tarjetas if item['titulo'].lower() == title.lower()]
    if not datos:
        return HttpResponse('Not Found', status=404)
    else:
        item = datos[0]
        return render(request, "core/detalle_mas_info.html", {"datos_tarjeta":item})


