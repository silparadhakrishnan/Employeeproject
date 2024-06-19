from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class EmployeeModel(AbstractUser):
    age=models.IntegerField()
    phone=models.CharField(max_length=100)
    department=models.CharField(max_length=100) 
    designation=models.CharField(max_length=100)