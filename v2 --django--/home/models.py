from django.db.models.deletion import CASCADE
from Wild_Fang.settings import DEFAULT_AUTO_FIELD
from django.db import models

# Create your models here.

class Genero(models.Model):
    idGenero = models.IntegerField(primary_key=True,verbose_name='Id de Genero')
    nombre = models.CharField(max_length=50, verbose_name='Nombre Genero')

class Marca(models.Model):
    idMarca = models.IntegerField(primary_key=True, verbose_name='Id de Marca')
    nombreMarca = models.CharField(max_length=50, verbose_name='Nombre Marca')

class Zapatilla(models.Model):
    idZapatilla = models.IntegerField(primary_key=True, verbose_name='Id de Zapatilla')
    modelo = models.CharField(max_length=50, verbose_name='Modelo de Zapatilla')
    descripcion = models.TextField(verbose_name='Descripcion Zapatilla')
    precio = models.IntegerField(verbose_name='Precio Zapatilla')
    foto = models.ImageField(upload_to='Zapas',verbose_name='Foto de Zapatilla')
    genero = models.ForeignKey(Genero,on_delete=models.CASCADE)
    marca = models.ForeignKey(Marca,on_delete=models.CASCADE)

class Usuario(models.Model):
    rut = models.CharField(max_length=13,primary_key=True,verbose_name='Rut de Usuario')
    nombre = models.CharField(max_length=50,verbose_name='Nombre de Usuario')
    apellido = models.CharField(max_length=50,verbose_name='Apellido Usuario')
    fecha_nac = models.DateField(verbose_name='Fecha nacimiento de Usuario')
    mail =  models.CharField(max_length=50,verbose_name='Correo electronico Usuario')
    password = models.CharField(max_length=50,verbose_name='Contraseña Usuario')
    nomUsuario = models.CharField(max_length=50,verbose_name='Nombre de Cuenta de Usuario')
    tipoUsuario = models.CharField(max_length=50,verbose_name='Tipo de Usuario')

class MetodoPago(models.Model):
    idMetodo = models.IntegerField(primary_key=True,verbose_name='Id de Metodo')
    metodo = models.CharField(max_length=50,verbose_name='Metodo de Pago')

class Pedido(models.Model):
    idPedido = models.IntegerField(primary_key=True,verbose_name='Id de Pedido')
    fecha = models.DateField(verbose_name='Fecha Pedido')
    total = models.IntegerField(verbose_name='Precio total')
    metodopago = models.ForeignKey(MetodoPago,on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE)

class Stock(models.Model):
    idStock = models.IntegerField(primary_key=True, verbose_name='Id Stock')
    talla = models.IntegerField(verbose_name='Talla de Zapatilla')
    cantidad = models.IntegerField(verbose_name='Cantidad de Zapatilla en stock')
    zapatilla = models.ForeignKey(Zapatilla,on_delete=models.CASCADE)

class Detalle(models.Model):
    idDetalle = models.IntegerField(primary_key=True,verbose_name='Id de Detalle')
    subTotal = models.IntegerField(verbose_name='Sub total de Compra')
    cantidad = models.IntegerField(verbose_name='Cantidad de Zapatillas compradas')
    pedido = models.ForeignKey(Pedido,on_delete=models.CASCADE)
    zapatilla = models.ForeignKey(Zapatilla,on_delete=models.CASCADE)

class Direccion(models.Model):
    idDireccion = models.IntegerField(primary_key=True,verbose_name='Id de Direccion')
    calle = models.CharField(max_length=50,verbose_name='Nombre de la calle')
    numero = models.IntegerField(verbose_name='Numero de la casa')

class Region(models.Model):
    idRegion = models.IntegerField(primary_key=True,verbose_name='Id de Region')
    nombreRegion = models.CharField(max_length=70,verbose_name='Nombre de la Region')

class Comuna(models.Model):
    idComuna = models.IntegerField(primary_key=True,verbose_name='Id de Comuna')
    nombreComuna = models.CharField(max_length=70,verbose_name='Nombre de la Comuna')
    region = models.ForeignKey(Region,on_delete=models.CASCADE)
