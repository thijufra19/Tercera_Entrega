from django.urls import path
from Gestion_Pedidos import views

urlpatterns = [
    
    path('', views.inicio, name="Inicio"),
    path('nosotros', views.nosotros, name="Nosotros"),
    path('servicios', views.servicios, name="Servicio"),
    path('productos', views.productos, name="Productos"),
    path('reservas', views.reservas, name="Reservas"),
    path('contactos', views.contactos, name="Contactos"),
    path('busqueda_servicios/', views.busqueda_servicios),
    path('buscar/', views.buscar),
    
]