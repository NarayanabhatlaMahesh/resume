from django.db import models
from django.forms import ModelForm

class Heading(models.Model):
    name = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=100)
    email_id = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    summary = models.TextField()

class Skills(models.Model):
    skill_name = models.CharField(max_length=100)
    strength = models.IntegerField()

class ExtraCurriculars(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)

class Projects(models.Model):
    name = models.CharField(max_length=100)
    start_duration = models.DateField()
    end_duration = models.DateField()
    about = models.TextField()

class Education(models.Model):
    name = models.CharField(max_length=100)
    start_duration = models.DateField()
    end_duration = models.DateField()
    score = models.IntegerField()
    course_name = models.CharField(max_length=100)


class EducationForm(ModelForm):
    class Meta:
        model = Education
        fields=['name', 'start_duration', 'end_duration' ,'score', 'course_name']