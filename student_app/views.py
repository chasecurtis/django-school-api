from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Student
from .serializers import StudentAllSerializer

# Create your views here.


class All_students(APIView):
    def get(self, request):
        students = Student.objects.all()
        serialized_students = StudentAllSerializer(students, many=True)
        return Response(serialized_students.data)


class A_student(APIView):
    def get(self, request, id):
        student = get_object_or_404(Student, id=id)
        serialized_student = StudentAllSerializer(student)
        return Response(serialized_student.data)
