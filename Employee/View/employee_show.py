from Employee.Serializer.Employee_Registration import EmployeeCreateSerializer,EmployeeUpdateSerializer
from Employee.models import User 
from rest_framework import generics
from rest_framework.permissions import IsAdminUser


class Employee_list_api(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class=EmployeeCreateSerializer


class Employee_update_information_API(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class=EmployeeUpdateSerializer


class Employee_update_retrieve_information_api(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class=EmployeeCreateSerializer


class EmployeeDelete_API_view(generics.DestroyAPIView):
    queryset = User.objects.all()
    permission_classes =[IsAdminUser]
    serializer_class = EmployeeCreateSerializer

