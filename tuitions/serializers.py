from rest_framework import serializers
from . import models

class StudentClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.StudentClass
        fields = '__all__'

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Subject
        fields = '__all__'

class TuitionSerializer(serializers.ModelSerializer):
    student_class = serializers.StringRelatedField(many=False)
    tutor = serializers.StringRelatedField(many=False)
    class Meta:
        model = models.Tuition
        fields = '__all__'