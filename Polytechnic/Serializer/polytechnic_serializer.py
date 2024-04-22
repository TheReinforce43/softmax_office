from rest_framework import serializers
from Polytechnic.Model.polytechnic_model import PolytechnicModel
from Polytechnic.Model.location import LocationModel


class PolytechnicSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=PolytechnicModel
        fields='__all__'

class LocationSerializer(serializers.ModelSerializer):
    polytechnic_details=PolytechnicSerializer(read_only=True,many=True)
    class Meta:
        model=LocationModel
        fields='__all__'


