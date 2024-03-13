from django.db import models

# Create your models here.
class Insumo(models.Model):
    nombre=models.CharField(max_length=50)
    costo=models.IntegerField()
    cantidad=models.IntegerField()

class Personal(models.Model):
    nombre=models.CharField(max_length=50)
    sueldo=models.IntegerField()

class Cliente(models.Model):
    nombre=models.CharField(max_length=50)
    consumo=models.IntegerField()
    tipodepago=models.CharField(max_length=50)