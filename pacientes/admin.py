from django.contrib import admin
from .models import Paciente, Usuario, Direccion, Ocupacion, SeguroSalud, DatosEmergencia

# Register your models here.
admin.site.register(Paciente)
admin.site.register(Usuario)
admin.site.register(Direccion)
admin.site.register(Ocupacion)
admin.site.register(SeguroSalud)
admin.site.register(DatosEmergencia)