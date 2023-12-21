from rest_framework import serializers
from APP_FINAL.models import models_inscritos, models_instituciones

class InstitucionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models_instituciones
        fields = '__all__'

class InscritosSerializer(serializers.ModelSerializer):
    institucion_nombre = serializers.CharField(source='institucion.nombre', read_only=True)

    class Meta:
        model = models_inscritos
        fields = ['id', 'nombre', 'telefono', 'fecha_inscripcion', 'institucion_nombre', 'hora_inscripcion', 'estado', 'observacion']