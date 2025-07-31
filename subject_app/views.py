from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Subject
from .serializers import SubjectSerializer

# Create your views here.


class All_subjects(APIView):
    def get(self, request):
        subjects = Subject.objects.all()
        serialized_subjects = SubjectSerializer(subjects, many=True)
        return Response(serialized_subjects.data)


class A_subject(APIView):
    def get(self, request, subject):
        subject_obj = get_object_or_404(Subject, subject_name__iexact=subject)
        serialized_subject = SubjectSerializer(subject_obj)
        return Response(serialized_subject.data)
