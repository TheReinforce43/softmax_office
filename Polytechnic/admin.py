from django.contrib import admin
from Polytechnic.Model.polytechnic_model import PolytechnicModel
from Polytechnic.Model.location import LocationModel
from Polytechnic.Model.institute_department_details import Department_Detail


admin.site.register(PolytechnicModel)
admin.site.register(LocationModel)
admin.site.register(Department_Detail)
