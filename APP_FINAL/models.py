from django.utils import timezone
from django.db import models



class models_instituciones(models.Model):
        id=models.AutoField(primary_key=True)
        nombre=models.CharField(max_length=80)
        def __str__(self):
                return self.nombre

class models_inscritos(models.Model):
        elegir_estado = [
            ('reservado', 'RESERVADO'),
            ('completada', 'COMPLETADA'),
            ('anulada', 'ANULADA'),
            ('no asisten','NO ASISTEN')
        ]

        id=models.AutoField(primary_key=True)
        nombre=models.CharField(max_length=80)
        telefono=models.IntegerField()  
        fecha_inscripcion=models.DateField(auto_now_add=True)
        institucion=models.ForeignKey(models_instituciones,on_delete=models.PROTECT,null=True)
        hora_inscripcion=models.TimeField(auto_now_add=True)
        estado=models.CharField(max_length = 20, choices = elegir_estado)
        observacion=models.CharField(max_length=300,blank=True)
       
      





