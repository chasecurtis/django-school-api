from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin", admin.site.urls),
    path("api/v1/students/", include("student_app.urls")),
    path("api/v1/subjects/", include("subject_app.urls")),
]
