from django.db import models 

class CategoryModel(models.Model):
    mode=[
        ('ON','ON'),
        ('OFF','OFF'),
    ]
    category_name=models.CharField(max_length=150,unique=True)
    status=models.CharField(max_length=10,choices=mode)

    def __str__(self) -> str:
        return self.category_name
