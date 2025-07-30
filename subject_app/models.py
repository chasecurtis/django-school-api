from django.db import models
from django.db import models
from django.utils import timezone
from django.core import validators as v
from .validators import validate_professor_name, validate_subject_format

# from student_app.models import Student


# Create your models here.
class Subject(models.Model):
    subject_name = models.CharField(
        unique=True, blank=False, null=False, validators=[validate_subject_format]
    )
    professor = models.CharField(
        default="Mr. Cahan",
        blank=False,
        null=False,
        validators=[validate_professor_name],
    )
    # students = models.ManyToManyField(Student, related_name="subjects")

    def __str__(self):
        return f"{self.subject_name} - {self.professor} - {self.students.count}"

    def add_a_student(self, student_id):
        if self.students.count() < 31:
            self.students.add(student_id)
        else:
            raise Exception("This subject is full!")

    def drop_a_student(self, student_id):
        if self.students.count() > 0:
            self.students.remove(student_id)
        else:
            raise Exception("This subject is empty!")
