from io import StringIO
from typing import MutableMapping
from django.shortcuts import redirect, render
from .models import Genero, Marca, Usuario, Zapatilla
from django.contrib import messages
from django.db.models.functions import ExtractYear
# Create your views here.
def index(request):
    return render(request,'home/index.html')
####    PAGINA PRINCIPAL INDEX #####
def blazer(request):
    return render(request,'home/hombre/blazer.html')
def crater(request):
    return render(request,'home/hombre/crater.html')
def energyx(request):
    return render(request,'home/hombre/energyx.html')
def hombres(request):
    return render(request,'home/hombre/hombres.html')
def m(request):
    return render(request,'home/hombre/m.html')
def mid_air_red(request):
    return render(request,'home/hombre/mid-air-red.html')
def quest3(request):
    return render(request,'home/hombre/quest3.html')
def titan(request):
    return render(request,'home/hombre/titan.html')
####    PAGINA HOMBRE Y MODELOS #####
def mujeres(request):
    return render(request,'home/mujer/mujeres.html')
def PM1(request):
    return render(request,'home/mujer/PM1.html')
def PM2(request):
    return render(request,'home/mujer/PM2.html')
def PM3(request):
    return render(request,'home/mujer/PM3.html')
def PM4(request):
    return render(request,'home/mujer/PM4.html')
def PM5(request):
    return render(request,'home/mujer/PM5.html')
def PM6(request):
    return render(request,'home/mujer/PM6.html')
def PM7(request):
    return render(request,'home/mujer/PM7.html')
def PM8(request):
    return render(request,'home/mujer/PM8.html')
####    PAGINA MUJERES Y MODELOS #####
def ninos(request):
    return render(request,'home/ninio/ninos.html')
def m1(request):
    return render(request,'home/ninio/m1.html')
def stmlur(request):
    return render(request,'home/ninio/stlmur.html')
def dc(request):
    return render(request,'home/ninio/dc.html')
def teamcourt(request):
    return render(request,'home/ninio/teamcourt.html')
def xray(request):
    return render(request,'home/ninio/xray.html')
####    PAGINA NIÑOS Y MODELOS #####
def contacto(request):
    return render(request,'home/contacto.html')
def recuperar(request):
    return render(request,'home/recuperar.html')
def crear_cuenta(request):
    return render(request,'home/crear_cuenta.html')
####    PAGINAS DE MANEJO DE CUENTAS#####

####    INSERCION DE DATOS  ####
def listar(request):
    generos = Genero.objects.all()
    marcas = Marca.objects.all()
    contexto = {'generos':generos,'marcas':marcas}
    return render(request, 'home/agregar_datos.html', contexto)


def regZap(request):
    newIdZapatilla = request.POST['idZapatilla']
    newModelo = request.POST['modelo']
    newDescripcion = request.POST['descripcion']
    newPrecio = request.POST['precio']
    newFoto = request.FILES['foto']
    newGenero = request.POST['genero']
    newMarca = request.POST['marca']

    genero_eleg = Genero.objects.get(idGenero = newGenero)
    marca_eleg = Marca.objects.get(idMarca = newMarca)

    Zapatilla.objects.create(idZapatilla = newIdZapatilla, modelo = newModelo, 
                             descripcion = newDescripcion, precio = newPrecio,
                             foto = newFoto, genero = genero_eleg, marca = marca_eleg)
    return redirect(listar)

def regMarca(request):
    idMarca = request.POST['idMarca']
    nombreMarca = request.POST['nombreMarca']

    Marca.objects.create(idMarca = idMarca, nombreMarca = nombreMarca)
    return redirect(listar)

def regUser(request):
    rut = request.POST['rut']
    nombre = request.POST['nombre']
    apellido = request.POST['apellido']
    fecha_nac = request.POST['fechaNac']
    mail = request.POST['mail']
    password = request.POST['clave']
    nomUsuario = rut[0:2] + nombre[0:4] + apellido[0:2] + fecha_nac[0:4]
    tipoUsuario = 'cliente'
    Usuario.objects.create(rut = rut, nombre = nombre, apellido = apellido, fecha_nac = fecha_nac, mail = mail,
                           password = password, nomUsuario = nomUsuario, tipoUsuario = tipoUsuario)
    return redirect(crear_cuenta)