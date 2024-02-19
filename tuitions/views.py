from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializers
# Create your views here.
class StudentClassViewset(viewsets.ModelViewSet):
    queryset = models.StudentClass.objects.all()
    serializer_class=serializers.StudentClassSerializer

class SubjectViewset(viewsets.ModelViewSet):
    queryset = models.Subject.objects.all()
    serializer_class=serializers.SubjectSerializer

class TuitionViewset(viewsets.ModelViewSet):
    queryset = models.Tuition.objects.all()
    serializer_class=serializers.TuitionSerializer