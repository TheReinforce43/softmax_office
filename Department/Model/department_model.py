from django.db import models 


class DepartmentModel(models.Model):
    full_name=models.CharField(max_length=150,unique=True)
    short_name=models.CharField(max_length=10,unique=True)
    code=models.CharField(max_length=15,null=True,blank=True)
    

    def __str__(self) -> str:
        return self.short_name