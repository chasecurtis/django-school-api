from django.shortcuts import render
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
