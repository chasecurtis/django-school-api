from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_201_CREATED,
    HTTP_204_NO_CONTENT,
    HTTP_400_BAD_REQUEST,
)

from .models import Grade
from .serializers import GradeSerializer


class All_grades(APIView):
    def get(self, request):
        grades = Grade.objects.all()
        ser_grades = GradeSerializer(grades, many=True)
        return Response(ser_grades.data)

    def post(self, request):
        ser_grade = GradeSerializer(data=request.data)
        if ser_grade.is_valid():
            ser_grade.save()
            return Response(ser_grade.data, status=HTTP_201_CREATED)
        return Response(ser_grade.errors, status=HTTP_400_BAD_REQUEST)


class A_grade(APIView):
    def get(self, request, id):
        grade = get_object_or_404(Grade, id=id)
        ser_grade = GradeSerializer(grade)
        return Response(ser_grade.data)

    def put(self, request, id):
        grade = get_object_or_404(Grade, id=id)
        ser_grade = GradeSerializer(grade, data=request.data, partial=True)
        if ser_grade.is_valid():
            ser_grade.save()
            return Response(status=HTTP_204_NO_CONTENT)
        return Response(ser_grade.errors, status=HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        grade = get_object_or_404(Grade, id=id)
        grade.delete()
        return Response(status=HTTP_204_NO_CONTENT)
