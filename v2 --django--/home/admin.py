from django.contrib import admin
from .models import Direccion,Genero, Marca, MetodoPago, Region,Usuario,Zapatilla,Stock, Pedido, Detalle,Comuna

# Register your models here.
admin.site.register(Direccion)
admin.site.register(Genero)
admin.site.register(Marca)
admin.site.register(MetodoPago)
admin.site.register(Usuario)
admin.site.register(Zapatilla)
admin.site.register(Stock)
admin.site.register(Pedido)
admin.site.register(Detalle)
admin.site.register(Comuna)
admin.site.register(Region)