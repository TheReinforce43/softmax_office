from django.db import models 
from Polytechnic.Model.location import LocationModel

class PolytechnicModel(models.Model):
    INSTITUTE_TYPES = (
        ('public', 'Public'),
        ('private', 'Private'),
    )
    name = models.CharField(max_length=100, unique=True)
    location = models.ForeignKey(LocationModel,on_delete=models.SET_NULL,related_name='polytechnic_details',null=True)
    institute_type = models.CharField(choices=INSTITUTE_TYPES, max_length=15)

    def __str__(self):
        return self.name



