from django.db import models 
from Employee.models import User 
from Polytechnic.Model.polytechnic_model import PolytechnicModel

class StudentModel(models.Model):

    Semesters=[
        ('1','One'),
        ('2','Two'),
        ('3','Three'),
        ('4','Four'),
        ('5','Five'),
        ('6','Six'),
        ('7','Seven'),
        
    ]

    Probhidhans=[
        ('2022','2022'),
        ('2016','2016'),
        ('2010','2010'),
    ]

    Dreams=[
        ('DUET','DUET'),
        ('GOVT-JOB','GOVT-JOB'),
    ]
    Secondary_Education=[
        ('SSC','SSC'),
        ('DAKHIL','DAKHIL'),
        ('VOCATIONAL','VOCATIONAL'),
    ]

    Session=[
        ('2016-17','2016-17'),
        ('2017-18','2017-18'),
        ('2018-19','2018-19'),
        ('2019-20','2019-20'),
        ('2020-21','2020-21'),
        ('2021-22','2021-22'),
        ('2022-23','2022-23'),
        ('2023-24','2023-24'),
    ]

    # user_student=models.OneToOneField(User,related_name="student_account",on_delete=models.CASCADE)
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    phone_number=models.CharField(max_length=20,unique=True)
    second_phone_number=models.CharField(max_length=20,unique=True,null=True,blank=True)
    email=models.EmailField(max_length=200,null=True,blank=True,unique=True)
    # polytechnic=models.ForeignKey(PolytechnicModel, related_name="polytechnic_student",on_delete=models.SET_NULL, null=True)
    # department=models.ForeignKey(DepartmentModel, related_name="department_student", on_delete=models.SET_NULL, null=True)
    polytechnic_board_roll=models.IntegerField(unique=True)
    session=models.CharField(max_length=20,choices=Session,default='2023-24')
    is_stippend=models.BooleanField(default=False)
    number_of_refferds=models.IntegerField(default=0)
    semester=models.CharField(max_length=3,choices=Semesters,default='1')
    probhidhan=models.CharField(max_length=5,choices=Probhidhans,default='2022')
    secondary_education=models.CharField(max_length=30,choices=Secondary_Education,default='SSC')
    secondary_gpa=models.FloatField(default=0)
    dream=models.CharField(max_length=10,choices=Dreams,default=None,null=True)
    
