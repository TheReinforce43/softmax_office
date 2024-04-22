from rest_framework import generics
from Department.Model.department_model import DepartmentModel
from Department.Serializer.department_serializer import DepartmentSerializer


class department_list_create_api(generics.ListCreateAPIView):
    queryset=DepartmentModel.objects.all()
    serializer_class=DepartmentSerializer


class department_update_retrieve_api(generics.RetrieveUpdateAPIView):
    queryset=DepartmentModel.objects.all()
    serializer_class=DepartmentSerializer
    
