from dataclasses import field
from rest_framework import serializers

from .models import *


class TankSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tank
        fields = ('name', 'type', 'description',
                  'armament', 'equipment', 'feature')


class AircraftSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Aircraft
        fields = ('name', 'type', 'description',
                  'armament', 'equipment', 'feature')
