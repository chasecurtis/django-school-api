from django.db import models


# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    student_email = models.EmailField(unique=True, blank=False, null=False)
    personal_email = models.EmailField(unique=True, blank=True, null=True)
    locker_number = models.IntegerField(
        unique=True, blank=False, null=False, default=110
    )
    locker_combination = models.CharField(
        blank=False, null=False, max_length=8, default="12-12-12"
    )
    good_student = models.BooleanField(blank=False, null=False, default=True)

    def __str__(self):
        return f"{self.name} - {self.student_email} - {self.locker_number}"

    def locker_reassignment(self, new_locker_number: int):
        self.locker_number = new_locker_number
        self.save()

    def student_status(self, is_good: bool):
        self.good_student = is_good
        self.save()
