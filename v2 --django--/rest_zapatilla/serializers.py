from django.db.models.base import Model
from home.models import Zapatilla
from rest_framework import serializers

class ZapatillaSerializador(serializers.ModelSerializer):
    class Meta:
        model = Zapatilla
        fields = ['idZapatilla','modelo','descripcion','precio','foto','genero','marca']