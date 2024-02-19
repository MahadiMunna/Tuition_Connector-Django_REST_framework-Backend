from rest_framework import serializers
from . import models

class TutorSerializer(serializers.ModelSerializer):
    tutor = serializers.StringRelatedField(many=False)
    class Meta:
        model = models.TutorAccount
        fields = '__all__'