from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse

from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from .serializers import *  # import the serializer we just created
from .models import *

# Create your views here.


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
@csrf_exempt
def get_aircraft_information_api(request):
    if request.method == 'GET':
        vehicles = Aircraft.objects.all().order_by('id')
        vehicles_serializer = AircraftSerializer(vehicles, many=True)
        return JsonResponse(vehicles_serializer.data, safe=False)


@csrf_exempt
def get_aircraft_information_by_name_api(request, name='name'):
    if request.method == 'GET':
        vehicles = Aircraft.objects.all().order_by('id').filter(name=name)
        vehicles_serializer = AircraftSerializer(vehicles, many=True)
        return JsonResponse(vehicles_serializer.data, safe=False)


@csrf_exempt
def get_aircraft_information_by_id_api(request, id=0):
    if request.method == 'GET':
        vehicles = Aircraft.objects.all().filter(id=id)
        vehicles_serializer = AircraftSerializer(vehicles, many=True)
        return JsonResponse(vehicles_serializer.data, safe=False)


@csrf_exempt
def post_aircraft_information_api(request):
    if request.method == 'POST':
        vehicle_data = JSONParser().parse(request)
        vehicles_serializer = AircraftSerializer(data=vehicle_data)
        if vehicles_serializer.is_valid():
            vehicles_serializer.save()
            return JsonResponse(f"Added Aircraft {vehicle_data['name']} Successfully", safe=False)
        return JsonResponse('Failed to Add', safe=False)


@csrf_exempt
def put_aircraft_information_api(request, id=0):
    if request.method == 'PUT':
        vehicle_data = JSONParser().parse(request)
        vehicle = Aircraft.objects.get(id=id)
        vehicles_serializer = AircraftSerializer(vehicle, data=vehicle_data)
        if vehicles_serializer.is_valid():
            vehicles_serializer.save()
            return JsonResponse('Updated Aircraft Successfully', safe=False)
        return JsonResponse('Failed to Update Aircraft')


@csrf_exempt
def delete_aircraft_information_api(request, id=0):
    if request.method == 'DELETE':
        vehicle = Aircraft.objects.get(id=id)
        vehicle.delete()
        return JsonResponse(f'Deleted Aircraft with id {id} Successfully', safe=False)


def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())
