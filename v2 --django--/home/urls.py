from home.models import Direccion, Pedido
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth.decorators import login_required
from .views import  direccion, datos, infoTalla, mid_air_blue, mid_air_gray, mid_air_purple, mostrarZapatilla, ordenLista, talla, buscar, carrito, direccionUsuario, editarMarca, editarMarcaSql, editarStock, editarStockSql, editarZap,editarLista, editarZapSql, eliminarCarrito, eliminarDireccion, eliminarMarca, eliminarStock, eliminarZap, index,hombres,listar, login_view, logout_view, mid_air_red, modificarUsuario, procesarPedido, regStock,regMarca, regUser,regZap,mujeres,ninos, usuario,contacto,recuperar,crear_cuenta

urlpatterns = [
    path('', index, name="index"),
    path('editarZap/<int:id>', editarZap, name="editarZap"),
    path('editarZapSql', editarZapSql, name="editarZapSql"),
    path('editarLista', editarLista, name="editarLista"),
    path('eliminarZap/<int:id>', eliminarZap, name="eliminarZap"),
    path('editarMarca/<int:id>', editarMarca, name="editarMarca"),
    path('editarMarcaSql', editarMarcaSql, name="editarMarcaSql"),
    path('eliminarMarca/<int:id>', eliminarMarca, name="eliminarMarca"),
    path('editarStock/<int:id>', editarStock, name="editarStock"),
    path('editarStockSql', editarStockSql, name="editarStockSql"),
    path('eliminarStock/<int:id>', eliminarStock, name="eliminarStock"),
    path('hombres', hombres, name="hombres"),
    path('mujeres', mujeres, name="mujeres"),
    path('mostrarZapatilla/<int:id>',mostrarZapatilla,name='mostrarZapatilla'),
    path('direccion', direccion, name="direccion"),
    path('datos', datos, name="datos"),
    path('ninos', ninos, name="ninos"),
    path('contacto', contacto, name="contacto"),
    path('recuperar', recuperar, name="recuperar"),
    path('crear_cuenta', crear_cuenta, name="crear_cuenta"),
    path('regZap', regZap, name='regZap'),
    path('formulario',listar,name='formulario'),
    path('regMarca',regMarca,name='regMarca'),
    path('regUser',regUser,name='regUser'),
    path('regStock',regStock,name='regStock'),
    path('buscar',buscar,name='buscar'),
    path('carrito',carrito,name='carrito'),
    path('procesarPedido',procesarPedido,name='procesarPedido'),
    path('mid_air_red',mid_air_red,name='mid_air_red'),
    path('mid_air_purple',mid_air_purple,name='mid_air_purple'),
    path('mid_air_blue',mid_air_blue,name='mid_air_blue'),
    path('mid_air_gray',mid_air_gray,name='mid_air_gray'),
    path('login/', LoginView.as_view(template_name='home/crear_cuenta.html'),name='login'),
    path('sesion', login_view ,name='sesion'),
    path('ordenLista', ordenLista ,name='ordenLista'),
    path('logout', logout_view ,name='logout'),
    path('usuario',login_required(usuario), name='usuario'),
    path('talla/<int:id>', talla, name='talla'),
    path('infoTalla/<int:id>', infoTalla, name='infoTalla'),
    path('direccionUsuario', direccionUsuario, name='direccionUsuario'),
    path('modificarUsuario/<rut>', modificarUsuario, name='modificarUsuario'),
    path('eliminarDireccion/<int:id>', eliminarDireccion, name='eliminarDireccion'),
    path('eliminarCarrito/<int:id>/<int:talla>',eliminarCarrito,name='eliminarCarrito')
]   
