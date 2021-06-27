from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    class_name  = models.CharField(max_length=30)
    roll_no = models.CharField(max_length=30)
