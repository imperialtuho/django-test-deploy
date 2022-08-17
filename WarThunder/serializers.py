from dataclasses import field
from rest_framework import serializers

from .models import *


common_data_dto = ('name', 'type', 'description',
                   'armament', 'equipment', 'feature')  # tube


class TankSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tank      # Model = <ModelClassName>
        fields = common_data_dto  # Return Data from Model entity


class AircraftSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Aircraft
        fields = common_data_dto  # Return Data from Model entity
