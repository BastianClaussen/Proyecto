from django.urls import path
from rest_zapatilla.views import vista_zapatilla, datos_zapatilla
from rest_zapatilla.viewslogin import login

urlpatterns = [
    path('lista_zapatilla',vista_zapatilla,name='lista_zapatilla'),
    path('datos_zapatilla/<int:id>',datos_zapatilla,name='datos_zapatilla'),
    path('login',login,name='login')
]   
