from django.db import models

# Create your models here.
class Paciente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.IntegerField()
    dni = models.IntegerField()
    telefono = models.IntegerField()
    email = models.EmailField()
    direccion = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    fecha_creacion = models.DateField(auto_now_add=True)
    numero_atencion = models.IntegerField()
    # como hacer primary key
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.nombre + ' ' + self.apellido