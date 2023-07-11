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
    
class Usuario(models.Model):
    primer_nombre = models.CharField(max_length=75, blank= False)
    segundo_nombre = models.CharField(max_length=75, blank= False)
    primer_apellido = models.CharField(max_length=75, blank= False)
    segundo_apellido = models.CharField(max_length=75,  blank= False)
    cedula = models.IntegerField(blank= False, unique=True)
    email = models.EmailField(unique=True, blank= False)
    telefono = models.IntegerField(blank= False)
    fecha_nacimiento = models.DateField(blank= False)
    lugar_nacimiento = models.CharField(max_length=75, blank= False)
    nacionalidad = models.CharField(max_length=75, blank= False)
    grupo_cultural = models.CharField(max_length=75, blank= False)
    edad = models.IntegerField()
    sexo = models.CharField(max_length=75, blank= False)
    estado_civil = models.CharField(max_length=75, blank= False)
    instruccion = models.CharField(max_length=75, blank= False)
    referido_de = models.CharField(max_length=75, blank= False)
    fecha_creacion = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.primer_nombre} {self.primer_apellido}'
    
class Direccion(models.Model):
    """  """
    direccion = models.CharField(max_length=150, blank= False)
    barrio = models.CharField(max_length=150, blank= False)
    parroquia = models.CharField(max_length=75, blank= False)
    canton = models.CharField(max_length=75, blank= False)
    provincia = models.CharField(max_length=75, blank= False)
    zona_rural = models.CharField(max_length=75, blank= False)
    fecha_creacion = models.DateField(auto_now_add=True)
    usuario_id = models.ForeignKey('Usuario', on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.barrio}'
    
    
class Ocupacion(models.Model):
    ocupacion = models.CharField(max_length=75, blank= False)
    empresa = models.CharField(max_length=75, blank= False)
    fecha_creacion = models.DateField(auto_now_add=True)
    usuario_id = models.ForeignKey('Usuario', on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.empresa}'
    
class SeguroSalud(models.Model):
    tipo_seguro_salud = models.CharField(max_length=75, blank= False)
    fecha_creacion = models.DateField(auto_now_add=True)
    usuario_id = models.ForeignKey('Usuario', on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.tipo_seguro_salud}'
    
class DatosEmergencia(models.Model):
    """  """
    numero_emergencia = models.IntegerField(blank= False)
    parentesco = models.CharField(max_length=75, blank= False)
    direccion = models.CharField(max_length=150, blank= False)
    nombre = models.CharField(max_length=75, blank= False)
    fecha_creacion = models.DateField(auto_now_add=True)
    usuario_id = models.ForeignKey('Usuario', on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.nombre}'