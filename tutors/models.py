from django.db import models
from django.contrib.auth.models import User
# Create your models here.
GENDER_TYPE = (
    ('Male', 'Male'),
    ('Female', 'Female'),
)
class TutorAccount(models.Model):
    tutor = models.OneToOneField(User, related_name='account', on_delete=models.CASCADE)
    gender = models.CharField(max_length=10, choices=GENDER_TYPE)
    educational_qualification = models.CharField(max_length= 100)
    institute=models.CharField(max_length=100)
    address = models.TextField(max_length=200)
    contact_no=models.CharField(max_length=100)

    def __str__(self):
        return f"{self.tutor.first_name} {self.tutor.last_name} - {self.educational_qualification} ({self.institute})"