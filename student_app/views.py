from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_201_CREATED,
    HTTP_204_NO_CONTENT,
    HTTP_400_BAD_REQUEST,
)
from .models import Student
from .serializers import StudentAllSerializer, StudentSerializer
from subject_app.models import Subject

# Create your views here.


class All_students(APIView):
    def get(self, request):
        students = Student.objects.all()
        serialized_students = StudentAllSerializer(students, many=True)
        return Response(serialized_students.data)

    def post(self, request):
        ser_student = StudentSerializer(data=request.data)
        if ser_student.is_valid():
            ser_student.save()
            return Response(ser_student.data, status=HTTP_201_CREATED)
        return Response(ser_student.errors, status=HTTP_400_BAD_REQUEST)


class A_student(APIView):
    def get(self, request, id):
        student = get_object_or_404(Student, id=id)
        serialized_student = StudentAllSerializer(student)
        return Response(serialized_student.data)

    def put(self, request, id):
        student = get_object_or_404(Student, id=id)
        ser_student = StudentSerializer(student, data=request.data, partial=True)
        if ser_student.is_valid():
            ser_student.save()
            return Response(status=HTTP_204_NO_CONTENT)
        return Response(ser_student.errors, status=HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        student = get_object_or_404(Student, id=id)
        student.delete()
        return Response(status=HTTP_204_NO_CONTENT)


class Add_subject(APIView):
    def post(self, request, student_id, subject_id):
        student = get_object_or_404(Student, id=student_id)
        subject = get_object_or_404(Subject, id=subject_id)
        try:
            student.add_subject(subject.id)
        except Exception as e:
            return Response({"detail": str(e)}, status=HTTP_400_BAD_REQUEST)
        serialized_student = StudentAllSerializer(student)
        return Response(serialized_student.data, status=HTTP_201_CREATED)
