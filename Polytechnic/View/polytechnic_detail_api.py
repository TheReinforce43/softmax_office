from rest_framework import generics
from Polytechnic.Model.institute_department_details import Department_Detail
from Polytechnic.Serializer.polytechnic_department_serializer import Polytechnic_Department_Details_Serializer

class Polytechnic_Department_Details_api(generics.ListCreateAPIView):
    queryset = Department_Detail.objects.all()
    serializer_class=Polytechnic_Department_Details_Serializer