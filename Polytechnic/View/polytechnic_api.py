from rest_framework import generics,viewsets
from Polytechnic.Model.location import LocationModel
from Polytechnic.Model.polytechnic_model import PolytechnicModel
from Polytechnic.Serializer.polytechnic_serializer import LocationSerializer,PolytechnicSerializer


class LocationAPI_all(viewsets.ModelViewSet):
    queryset = LocationModel.objects.all()
    serializer_class=LocationSerializer


class Polytechnic_list_create(generics.ListCreateAPIView):
    queryset = PolytechnicModel.objects.all()
    serializer_class=PolytechnicSerializer


class Polytechnic_update_retrive(generics.RetrieveUpdateAPIView):
    queryset = PolytechnicModel.objects.all()
    serializer_class=PolytechnicSerializer


    