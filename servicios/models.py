from django.db import models
from django.contrib import admin

class Cliente(models.Model):
    cliente  =   models.CharField(max_length=200)
    telefono  =   models.CharField(max_length=200)
    def __str__(self):
        return self.cliente

class Servicio(models.Model):
    nombre  =   models.CharField(max_length=200)
    def __str__(self):
        return self.nombre

class Carro(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    placa  =   models.CharField(max_length=100)
    marca =   models.CharField(max_length=200)
    linea  =   models.CharField(max_length=200)
    modelo = models.IntegerField()
    color  =   models.CharField(max_length=200)
    servicios   = models.ManyToManyField(Servicio, through='Detalle')
    def __str__(self):
        return self.placa

class Detalle (models.Model):
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)
    carro = models.ForeignKey(Carro, on_delete=models.CASCADE)

class DetalleInLine(admin.TabularInline):
    model = Detalle
    extra = 1

class ServicioAdmin(admin.ModelAdmin):
    inlines = (DetalleInLine,)

class CarroAdmin (admin.ModelAdmin):
    inlines = (DetalleInLine,)
