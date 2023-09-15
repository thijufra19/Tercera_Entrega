from django.contrib import admin
from Gestion_Pedidos.models import Clientes, Servicios, Pedido

# Register your models here.

class ClientesAdmin(admin.ModelAdmin):
    list_display=("nombre", "apellido", "telefono", "email")
    search_fields=("nombre", "apellido")

class ServicioAdmin(admin.ModelAdmin):
    list_filter=('seccion',)

class PedidoAdmin(admin.ModelAdmin):
    list_display=("numero", "Fecha")
    list_filter=('Fecha'),
    date_hierarchy=('Fecha')


admin.site.register(Clientes, ClientesAdmin)
admin.site.register(Servicios, ServicioAdmin)
admin.site.register(Pedido, PedidoAdmin)