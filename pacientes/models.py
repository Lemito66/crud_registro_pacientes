from django.db import models
# Create your models here.
class Paciente(models.Model):
    nombre = models.CharField(max_length=75 )
    apellido = models.CharField(max_length=75)
    edad = models.IntegerField()
    cedula = models.IntegerField()
    telefono = models.IntegerField()
    email = models.EmailField()
    direccion = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    fecha_creacion = models.DateField(auto_now_add=True)
    peso = models.IntegerField()
    altura = models.IntegerField()

    def __str__(self):
        return f'{self.nombre} {self.apellido}'