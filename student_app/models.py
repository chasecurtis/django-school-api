from django.db import models


# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=255)
    student_email = models.EmailField(unique=True, blank=False, null=False)
    personal_email = models.EmailField(unique=True, blank=False, null=False)
    locker_number = models.IntegerField(unique=True)
    locker_combination = models.CharField(max_length=8)
    good_student = models.BooleanField(default=True)
