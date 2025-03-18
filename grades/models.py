from django.db import models
from django.contrib.auth.models import User

class Grade(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    grade = models.CharField(max_length=10)
    date = models.DateTimeField(auto_now_add=True)

class Goal(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    target_grade = models.CharField(max_length=10)
    deadline = models.DateField()
    completed = models.BooleanField(default=False)

class History(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    action = models.CharField(max_length=200)
    timestamp = models.DateTimeField(auto_now_add=True)