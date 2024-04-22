from rest_framework import serializers
from Polytechnic.Model.institute_department_details import Department_Detail
from Department.Model.department_model import DepartmentModel

from Polytechnic.Serializer.polytechnic_serializer import PolytechnicSerializer
from Department.Serializer.department_serializer import DepartmentSerializer


class Polytechnic_Department_Details_Serializer(serializers.ModelSerializer):
    department_name=DepartmentSerializer(read_only=True,source='department_detail')
    polytechnic_name=PolytechnicSerializer(read_only=True,source='polytechnic_detail')

    class Meta:
        model=Department_Detail
        fileds='__all__'
