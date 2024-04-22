from django.db import models 

class LocationModel(models.Model):
    DIVISION=(
        ('Barishal','Barishal'),
        ('Chattogram','Chattogram'),
        ('Dhaka','Dhaka'),
        ('Khulna','Khulna'),
        ('Rajshahi','Rajshahi'),
        ('Rangpur','Rangpur'),
        ('Mymensingh','Mymensingh'),
        ('Sylhet','Sylhet'),
    )

    division=models.CharField(max_length=50,choices=DIVISION)
    district=models.CharField(max_length=150)

    def __str__(self) -> str:
        return f' Division: {self.division} || District: {self.district} '
    