from django.contrib import admin
from . import models
# Register your models here.

class SubjectAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('subject',)}
    list_display = ['subject','slug']
admin.site.register(models.Subject, SubjectAdmin)

class StudentClassAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('student_class',)}
    list_display = ['student_class','slug']
admin.site.register(models.StudentClass, StudentClassAdmin)

admin.site.register(models.Tuition)