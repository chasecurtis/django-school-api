from django.db import models
from django.utils import timezone
from django.core import validators as v
from subject_app.models import Subject
from .validators import (
    validate_name,
    validate_school_email,
    validate_combination_format,
)


# Create your models here.
class Student(models.Model):
    name = models.CharField(
        max_length=255, blank=False, null=False, validators=[validate_name]
    )
    student_email = models.EmailField(
        unique=True, blank=False, null=False, validators=[validate_school_email]
    )
    personal_email = models.EmailField(unique=True, blank=True, null=True)
    locker_number = models.IntegerField(
        unique=True,
        blank=False,
        null=False,
        default=110,
        validators=[v.MinValueValidator(1), v.MaxValueValidator(200)],
    )
    locker_combination = models.CharField(
        blank=False,
        null=False,
        default="12-12-12",
        validators=[validate_combination_format],
    )
    good_student = models.BooleanField(blank=False, null=False, default=True)
    subjects = models.ManyToManyField(Subject, related_name="students")

    def __str__(self):
        return f"{self.name} - {self.student_email} - {self.locker_number}"

    def locker_reassignment(self, new_locker_number: int):
        self.locker_number = new_locker_number
        self.save()

    def student_status(self, is_good: bool):
        self.good_student = is_good
        self.save()

    def add_subject(self, subject_id):
        subject_length = self.subjects.count()
        if subject_length < 8:
            self.subjects.add(subject_id)
        else:
            raise Exception("This students class schedule is full!")

    def remove_subject(self, subject_id):
        subject_length = self.subjects.count()
        if subject_length > 0:
            self.subjects.add(subject_id)
        else:
            raise Exception("This students class schedule is empty!")
