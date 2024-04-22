from rest_framework import serializers
from Department.Model.department_model import DepartmentModel


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model=DepartmentModel
        fields='__all__'
