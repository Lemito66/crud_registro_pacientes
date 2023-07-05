from rest_framework import serializers
from .models import Paciente
class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = '__all__'
        #fields = ('id', 'nombre', 'apellido', 'edad', 'cedula', 'telefono', 'email', 'direccion', 'fecha_nacimiento', 'fecha_creacion', 'peso', 'altura')