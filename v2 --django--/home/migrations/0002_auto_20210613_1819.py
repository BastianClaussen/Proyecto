# Generated by Django 3.2.3 on 2021-06-13 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detalle',
            name='subTotal',
            field=models.IntegerField(null=True, verbose_name='Sub total de Compra'),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='total',
            field=models.IntegerField(null=True, verbose_name='Precio total'),
        ),
    ]