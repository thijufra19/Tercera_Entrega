from django.shortcuts import render
from django.http import HttpResponse
from Gestion_Pedidos.models import Servicios
from Gestion_Pedidos.forms import FormularioContactos

# Create your views here.

def inicio(request):
    return render(request, 'Gestion_Pedidos/inicio.html')

def acerca_de(request):
    return render(request, 'Gestion_Pedidos/acerca_de.html')

def servicios(request):
    return render(request, 'Gestion_Pedidos/servicios.html')

def productos(request):
    return render(request, 'Gestion_Pedidos/productos.html')

def busqueda_servicios(request):
    return render(request, 'busqueda_servicios.html')

def buscar(request):

    if request.GET["serv"]:

        #mensaje = "servicio buscado: %r" %request.GET["serv"]
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
# def contacto(request):
#     if request.method == 'POST':

#         subject = 
#         message =
#         email = 
#         recipient_list =
#         send_email =

#         return render(request, "gracias.html")

#     return render(request, "contacto.html")

def contacto(request):

    if request.method=='POST':

        miFormulario = FormularioContactos(request.POST)

        if miFormularioF.is_valid():
            infForm = miFormulario.cleaned_data
            send_mail(infForm['asunto'], infForm['mensaje'], infForm.get('email', ''), ['thimago60@gmail.com'],)
            return render(request, "gracias.html")
    else:
        miFormulario = FormularioContactos()

return render(request, "formulario_contactos.html", {"form": miFormulario})






