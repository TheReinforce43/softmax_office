from django.db import models 
from django.contrib.auth.models import AbstractUser
from .Custom_Manager import UserManager

class User(AbstractUser):
    
    ROLE_CHOICES = (
        # ('admin', 'ADMIN'),
        ('marketer', 'MARKETER'),
        ('content_writer', 'CONTENT_WRITER'),
        ('support_teacher', 'SUPPORT_TEACHER'),
        ('video_editor', 'VIDEO_EDITER'),
        ('computer_operator', 'COMPUTER_OPERATOR'),
        ('software_engineer', 'SOFTWARE_ENGERER'),
    )

    username = None 
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=20, unique=True)
    role = models.CharField(max_length=30, choices=ROLE_CHOICES)
    

    def __str__(self) -> str:
        return self.email 
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'phone_number']
    objects=UserManager()