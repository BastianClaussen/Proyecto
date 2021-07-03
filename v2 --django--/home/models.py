from datetime import datetime
from django.db.models.deletion import CASCADE
from django.utils import tree
from Wild_Fang.settings import DEFAULT_AUTO_FIELD
from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Genero(models.Model):
    idGenero = models.AutoField(primary_key=True,verbose_name='Id de Genero')
    nombre = models.CharField(max_length=50, verbose_name='Nombre Genero')

class Marca(models.Model):
    idMarca = models.AutoField(primary_key=True, verbose_name='Id de Marca')
    nombreMarca = models.CharField(max_length=50, verbose_name='Nombre Marca')

class Zapatilla(models.Model):
    idZapatilla = models.AutoField(primary_key=True, verbose_name='Id de Zapatilla')
    modelo = models.CharField(max_length=50, verbose_name='Modelo de Zapatilla')
    descripcion = models.TextField(verbose_name='Descripcion Zapatilla')
    precio = models.IntegerField(verbose_name='Precio Zapatilla')
    foto = models.ImageField(upload_to='Zapas',verbose_name='Foto de Zapatilla',null= True)
    genero = models.ForeignKey(Genero,on_delete=models.CASCADE)
    marca = models.ForeignKey(Marca,on_delete=models.CASCADE)
    

class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rut = models.CharField(max_length=15)
    fecha_nacimiento = models.DateField(default="")

class MetodoPago(models.Model):
    idMetodo = models.AutoField(primary_key=True,verbose_name='Id de Metodo')
    metodo = models.CharField(max_length=50,verbose_name='Metodo de Pago')

class Region(models.Model):
    idRegion = models.IntegerField(primary_key=True,verbose_name='Id de Region')
    nombreRegion = models.CharField(max_length=70,verbose_name='Nombre de la Region')

class Comuna(models.Model):
    idComuna = models.IntegerField(primary_key=True,verbose_name='Id de Comuna')
    nombreComuna = models.CharField(max_length=70,verbose_name='Nombre de la Comuna')
    region = models.ForeignKey(Region,on_delete=models.CASCADE)

class Direccion(models.Model):
    idDireccion = models.AutoField(primary_key=True,verbose_name='Id de Direccion')
    calle = models.CharField(max_length=50,verbose_name='Nombre de la calle')
    numero = models.IntegerField(verbose_name='Numero de la casa')
    comuna = models.ForeignKey(Comuna,on_delete=models.CASCADE,null=True)
    region = models.ForeignKey(Region,on_delete=models.CASCADE,null=True)
    usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE,null=True)
    estado = models.IntegerField(verbose_name='Estado de la direccion')

class Pedido(models.Model):
    idPedido = models.AutoField(primary_key=True,verbose_name='Id de Pedido')
    fecha = models.DateField(default=datetime.now)
    total = models.IntegerField(verbose_name='Precio total',default=0,blank=True)
    metodopago = models.ForeignKey(MetodoPago,on_delete=models.CASCADE, default=1)
    usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE)
    direccion = models.ForeignKey(Direccion,on_delete=models.CASCADE, null=True)


class Stock(models.Model):
    idStock = models.AutoField(primary_key=True, verbose_name='Id Stock')
    talla = models.IntegerField(verbose_name='Talla de Zapatilla')
    cantidad = models.IntegerField(verbose_name='Cantidad de Zapatilla en stock')
    zapatilla = models.ForeignKey(Zapatilla,on_delete=models.CASCADE)

class Detalle(models.Model):
    idDetalle = models.AutoField(primary_key=True,verbose_name='Id de Detalle')
    subTotal = models.IntegerField(verbose_name='Sub total de Compra',default=0,blank=True)
    cantidad = models.IntegerField(verbose_name='Cantidad de Zapatillas compradas',default=0,blank=True)
    pedido = models.ForeignKey(Pedido,on_delete=models.CASCADE)
    zapatilla = models.ForeignKey(Zapatilla,on_delete=models.CASCADE)
    stock = models.ForeignKey(Stock,on_delete=models.CASCADE, null=True)




