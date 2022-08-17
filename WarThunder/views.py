from django.shortcuts import render
# Create your views here.
from rest_framework import viewsets
from .serializers import *  # import the serializer we just created
from .models import *
from rest_framework.response import Response


class TankViewSet(viewsets.ModelViewSet):
    # define queryset
    queryset = Tank.objects.all().order_by('name')
    serializer_class = TankSerializer


class AircraftViewSet(viewsets.ModelViewSet):
    # define queryset
    queryset = Aircraft.objects.all().order_by('name')
    serializer_class = AircraftSerializer
