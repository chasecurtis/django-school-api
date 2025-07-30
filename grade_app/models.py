from django.db import models
from django.db import models
from django.utils import timezone
from django.core import validators as v
from student_app.models import Student
from subject_app.models import Subject


# Create your models here.
class Grade(models.Model):
    grade = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=100,
        blank=False,
        null=False,
        validators=[v.MinValueValidator(0.00), v.MaxValueValidator(100.00)],
    )
    a_subject = models.ForeignKey(
        Subject, on_delete=models.SET_NULL, related_name="grades", null=True
    )
    student = models.ForeignKey(
        Student, on_delete=models.SET_NULL, related_name="grades", null=True
    )
