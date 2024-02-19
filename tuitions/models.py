from django.db import models
from tutors.models import TutorAccount
# Create your models here.
class StudentClass(models.Model):
    student_class = models.CharField(max_length = 20)
    slug = models.SlugField(max_length=100,unique=True, null=True, blank=True)

    def __str__(self) -> str:
        return self.student_class
    class Meta:
        verbose_name_plural = "Student Class"
    
class Subject(models.Model):
    subject = models.CharField(max_length = 50)
    slug = models.SlugField(max_length=100,unique=True, null=True, blank=True)

    def __str__(self) -> str:
        return self.subject

TUITION_TYPE = (
    ('Online', 'Online'),
    ('Offline', 'Offline'),    
)
MEDIUM = (
    ('Bangla', 'Bangla'),
    ('English', 'English'),    
)

class Tuition(models.Model):
    student_class=models.ForeignKey(StudentClass,on_delete=models.CASCADE)
    subject=models.ManyToManyField(Subject)
    medium=models.CharField(choices=MEDIUM, max_length=10)
    tuition_type=models.CharField(choices=TUITION_TYPE, max_length=10)
    location=models.CharField(max_length=100)
    tuition_details=models.TextField()
    time=models.CharField(max_length=20)
    salary=models.DecimalField(decimal_places=2,max_digits=10)
    availability=models.BooleanField(default=True)
    tutor=models.OneToOneField(TutorAccount, on_delete=models.CASCADE, blank=True, null=True)


    def __str__(self) -> str:
        subjects=[]
        status=""
        if self.availability:
            status="Available"
        else:
            status="Not available"
        for sub in self.subject.all():
            subjects.append(sub.subject)
        return f"Tuition - class {self.student_class}{subjects} at {self.location} [{self.time}] - {status}"
