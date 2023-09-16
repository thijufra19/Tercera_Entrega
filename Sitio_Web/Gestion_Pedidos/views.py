from django.shortcuts import render
from django.http import HttpResponse
from Gestion_Pedidos.models import Servicios
from Gestion_Pedidos.forms import FormularioContactos

# Create your views here.

def inicio(request):
    return render(request, "Menu/inicio.html")

def nosotros(request):
    return render(request, "Menu/nosotros.html")
    
def servicios(request):
    return render(request, "Menu/servicios.html")
    

def productos(request):
    return render(request, 'Menu/productos.html')

def reservas(request):
    return render(request, 'Menu/reservas.html')

def contactos(request):
    return render(request, 'Menu/contactos.html')

def busqueda_servicios(request):
    return render(request, 'busqueda_servicios.html')

def buscar(request):

    if request.GET["serv"]:
        servicio = request.GET["serv"]

        if len(servicio) > 20:
            mensaje = "Texto de busqueda demasiado largo"
        else: 
            servi = Servicios.objects.filter(nombre__icontains=servicio)

            return render(request, "resultados_busquedas.html", {"servicio": servi, "query": servicio})
    else:
         mensaje = "no ha introducido nada"

    return HttpResponse(mensaje)

""" leer la doc django para envio del form a mi correo de gmail """







