from django.db import models 
from Polytechnic.Model.polytechnic_model import PolytechnicModel
from Department.Model.department_model import DepartmentModel 

class Department_Detail(models.Model):
    department_name=models.ForeignKey(DepartmentModel,on_delete=models.SET_NULL,related_name='department_detail',null=True)
    polytechnic_name=models.ForeignKey(PolytechnicModel,on_delete=models.SET_NULL,related_name='polytechnic_detail',null=True)
    total_student=models.IntegerField(default=0)
    total_softmax_student=models.IntegerField(default=0)
    duetian_teacher=models.IntegerField(default=0)

    def __str__(self) -> str:
        return f'Department: {self.polytechnic_name} Polytechnic:{self.department_name}'