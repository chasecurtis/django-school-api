from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_201_CREATED,
    HTTP_204_NO_CONTENT,
    HTTP_400_BAD_REQUEST,
)
from .models import Subject
from .serializers import SubjectSerializer

# Create your views here.


class All_subjects(APIView):
    def get(self, request):
        subjects = Subject.objects.all()
        serialized_subjects = SubjectSerializer(subjects, many=True)
        return Response(serialized_subjects.data)

    def post(self, request):
        ser_subject = SubjectSerializer(data=request.data)
        if ser_subject.is_valid():
            ser_subject.save()
            return Response(ser_subject.data, status=HTTP_201_CREATED)
        return Response(ser_subject.errors, status=HTTP_400_BAD_REQUEST)


class A_subject(APIView):
    def get(self, request, subject):
        subject_obj = get_object_or_404(Subject, subject_name__iexact=subject)
        serialized_subject = SubjectSerializer(subject_obj)
        return Response(serialized_subject.data)

    def put(self, request, subject):
        subject_obj = get_object_or_404(Subject, subject_name__iexact=subject)
        ser_subject = SubjectSerializer(subject_obj, data=request.data, partial=True)
        if ser_subject.is_valid():
            ser_subject.save()
            return Response(status=HTTP_204_NO_CONTENT)
        return Response(ser_subject.errors, status=HTTP_400_BAD_REQUEST)

    def delete(self, request, subject):
        subject_obj = get_object_or_404(Subject, subject_name__iexact=subject)
        subject_obj.delete()
        return Response(status=HTTP_204_NO_CONTENT)
