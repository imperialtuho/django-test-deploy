from django.shortcuts import render

from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse

from rest_framework.parsers import JSONParser

from .serializers import *  # import the serializer we just created
from .models import *

# Create your views here.


@csrf_exempt
def aircraft_information_api(request, id=0, name='name'):
    if request.method == 'GET':
        vehicles = Aircraft.objects.all().order_by('id')
        vehicles_serializer = AircraftSerializer(vehicles, many=True)
        return JsonResponse(vehicles_serializer.data, safe=False)
    elif request.method == 'POST':
        vehicle_data = JSONParser().parse(request)
        vehicles_serializer = AircraftSerializer(data=vehicle_data)
        if vehicles_serializer.is_valid():
            vehicles_serializer.save()
            return JsonResponse('Added Successfully', safe=False)
        return JsonResponse('Failed to Add', safe=False)
    elif request.method == 'PUT':
        vehicle_data = JSONParser().parse(request)
        vehicle = Aircraft.objects.get(id=vehicle_data['id'])
        vehicles_serializer = AircraftSerializer(vehicle, data=vehicle_data)
        if vehicles_serializer.is_valid():
            vehicles_serializer.save()
            return JsonResponse('Updated Successfully', safe=False)
        return JsonResponse('Failed to Update')
    elif request.method == 'DELETE':
        vehicle = Aircraft.objects.get(id=id)
        vehicle.delete()
        return JsonResponse('Deleted Successfully', safe=False)
