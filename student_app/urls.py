from django.urls import path
from .views import All_students, A_student, Add_subject

urlpatterns = [
    path("", All_students.as_view(), name="all_students"),
    path("<int:id>/", A_student.as_view(), name="a_student"),
    path(
        "<int:student_id>/add-subject/<int:subject_id>/",
        Add_subject.as_view(),
        name="add_subject",
    ),
]
