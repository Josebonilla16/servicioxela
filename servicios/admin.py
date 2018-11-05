from django.contrib import admin
from servicios.models import Cliente, Servicio, ServicioAdmin, Carro, CarroAdmin
# Register your models here.
admin.site.register(Cliente)
admin.site.register(Servicio, ServicioAdmin)
admin.site.register(Carro, CarroAdmin)
