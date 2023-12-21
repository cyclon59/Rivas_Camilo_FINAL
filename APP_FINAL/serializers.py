from rest_framework import serializers
from APP_FINAL.models import models_inscritos,models_instituciones



class InstitucionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models_instituciones
        fields = '__all__'

class InscritosSerializer(serializers.ModelSerializer):
    class Meta:
        model = models_inscritos
        fields = '__all__'