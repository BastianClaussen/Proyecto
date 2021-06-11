from io import StringIO
from typing import MutableMapping
from django.shortcuts import redirect, render
from .models import Genero, Marca, Usuario, Zapatilla, Stock
from django.contrib import messages
# Create your views here.
def index(request):
    zapatillasHombre = Zapatilla.objects.filter(genero_id = 1)[:6]
    contexto = {'zapatillas':zapatillasHombre}
    return render(request, 'home/index.html', contexto)
####    PAGINA PRINCIPAL INDEX #####

def crater(request):
    return render(request,'home/hombre/crater.html')
def energyx(request):
    return render(request,'home/hombre/energyx.html')
def hombres(request):
    zapatillasHombre = Zapatilla.objects.filter(genero_id = 1)
    contexto = {'zapatillas':zapatillasHombre}
    return render(request,'home/hombre/hombres.html', contexto)
def m(request):
    return render(request,'home/hombre/m.html')
def mid_air_red(request):
    midAir = Zapatilla.objects.filter(pk=1)
    contexto = {'midAir':midAir}
    return render(request,'home/hombre/mid-air-red.html',contexto)
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
    return render(request,'home/ninio/stmlur.html')
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
    contexto = {'generos':generos,
                'marcas':marcas}
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

def regStock(request):
    idStock = request.POST['idStock']
    talla = request.POST['talla']
    cantidad = request.POST['cantidad']

    zapatilla = Zapatilla.objects.get(idZapatilla = request.POST['idZapatilla'])

    Stock.objects.create(idStock = idStock,talla = talla, cantidad = cantidad, zapatilla = zapatilla)
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

def mostrarZapatilla(request,id):
    zapatillas = Zapatilla.objects.get(idZapatilla = id)
    stock = Stock.objects.filter(zapatilla_id = id )
    contexto = {
        'zapatilla' : zapatillas,
        'stock' : stock,
    }

    return render(request,'home/zapatilla.html',contexto)


def editarLista(request):
    zapatillas = Zapatilla.objects.all()
    stock = Stock.objects.all()
    marca = Marca.objects.all()

    contexto = {
        'zapatilla' : zapatillas,
        'stock' : stock,
        'marca' : marca
    }

    return render(request,'home/mostrar.html',contexto)


def editarZap(request,id):
    zapMod = Zapatilla.objects.get(idZapatilla = id)
    genMod = Genero.objects.all()
    marcMod = Marca.objects.all()
    contexto = {
        'zapatilla' : zapMod,
        'genero' : genMod,
        'marca' : marcMod
    }
    return render(request,'home/modificar.html',contexto)


def editarZapSql(request):
    newidZapatilla = request.POST['idZapatilla']
    newModelo = request.POST['modelo']
    newDescripcion = request.POST['descripcion']
    newPrecio = request.POST['precio']
    newFoto = request.FILES['foto']
    newGenero = request.POST['genero']
    newMarca = request.POST['marca']

    newZapatilla = Zapatilla.objects.get(idZapatilla=newidZapatilla)

    newZapatilla.modelo = newModelo
    newZapatilla.descripcion = newDescripcion
    newZapatilla.precio = newPrecio
    newZapatilla.foto = newFoto

    genero = Genero.objects.get(idGenero = newGenero)
    marca = Marca.objects.get(idMarca = newMarca)

    newZapatilla.genero = genero
    newZapatilla.marca = marca
    newZapatilla.save()
    return redirect('editarLista')

def eliminarZap(request,id):
    zapatilla = Zapatilla.objects.get(idZapatilla = id)
    zapatilla.delete()

    return redirect('editarLista') 




def editarMarca(request,id):
    marca = Marca.objects.get(idMarca = id)
    contexto = {
        'marcas' : marca,
    }
    return render(request,'home/modificar.html',contexto)

def editarMarcaSql(request):
    newidMarca = request.POST['idMarca']
    newNombreMarca = request.POST['nombreMarca']

    newMarca = Marca.objects.get(idMarca=newidMarca)

    newMarca.nombreMarca = newNombreMarca

    newMarca.save()
    return redirect('editarLista')

def eliminarMarca(request,id):
    marca = Marca.objects.get(idMarca = id)
    marca.delete()

    return redirect('editarLista') 





def editarStock(request,id):
    stock = Stock.objects.get(idStock = id)
    zapatilla = Zapatilla.objects.all()
    contexto = {
        'stockf' : stock,
        'zapstock': zapatilla
    }
    return render(request,'home/modificar.html',contexto)

def editarStockSql(request):
    newidStock = request.POST['idStock']
    newCantidad = request.POST['cantidad']
    newtalla = request.POST['talla']

    newStock = Stock.objects.get(idStock=newidStock)

    idZapatilla = Zapatilla.objects.get(idZapatilla = request.POST['idZapatillaSt'])

    newStock.cantidad = newCantidad
    newStock.zapatilla = idZapatilla
    newStock.talla = newtalla

    newStock.save()
    return redirect('editarLista')

def eliminarStock(request,id):
    stock = Stock.objects.get(idStock = id)
    stock.delete()

    return redirect('editarLista') 

