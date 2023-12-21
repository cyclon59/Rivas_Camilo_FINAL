from django.shortcuts import render,redirect
from .models import models_inscritos,models_instituciones
from . import forms
from .forms import formu_inscritos,formu_instituciones
from .serializers import InscritosSerializer,InstitucionSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from django.http import Http404,JsonResponse


def index(request):
    return render(request, 'index.html')
def formulario(request):
    return render(request,'formulario.html')
def institucion(request):
    form = formu_instituciones()
    if request.method == 'POST':
        form = formu_instituciones(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = formu_instituciones()

    data = {'title': 'instituciones', 'formulario': form}
    return render(request, 'formulario.html', data)

def inscritos(request):
    if request.method == 'POST':
        form = formu_inscritos(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = formu_inscritos()

    data = {'title': 'inscritos', 'formulario': form}
    return render(request, 'formulario.html', data)

def usuario(request):
    data = {
        'RUT':'21.303.355-7',
        'Nombre': 'Camilo Rivas',
        'Sección': 'IEI-171-N4',
    }
    return JsonResponse(data)


class inscritosList_class(APIView):
    def get(self, request):
        inscritos =models_inscritos.objects.all()
        serial = InscritosSerializer(inscritos,many=True)
        return Response(serial.data)
    
    def post(self,request):
        serial = InscritosSerializer(data= request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data,status = status.HTTP_201_CREATED)
        return Response(serial.errors,status = status.HTTP_400_BAD_REQUEST)
    
class inscritos_detalle_class(APIView):
    def get_object(self, id):
        try:
            return models_inscritos.objects.get(pk=id)
        except models_inscritos.DoesNotExist:
            raise Http404()    
    def get(self,request,id):
        inscritos = self.get_object(id)
        serial = InscritosSerializer(inscritos)
        return Response(serial.data)
    
    def put (self,request,id):
        inscritos= self.get_object(id)
        serial = InscritosSerializer(inscritos,data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        inscritos = self.get_object(id)
        inscritos.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
@api_view(['GET','POST'])
def institucion_list(request):
    if request.method == 'GET':
        institucion = models_instituciones.objects.all()
        serial = InstitucionSerializer(institucion,many=True)
        return Response(serial.data)
    
    if request.method == 'POST':
        serial = InstitucionSerializer(data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data, status=status.HTTP_201_CREATED)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)

    
@api_view(['GET','PUT','DELETE'])
def institucion_detalle(request,id):
    try:
        institucion = models_instituciones.objects.get(pk=id)
    except models_instituciones.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serial = InstitucionSerializer(institucion)
        return Response(serial.data)
    if request.method == 'PUT':
        serial = InstitucionSerializer(institucion,data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        institucion.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

