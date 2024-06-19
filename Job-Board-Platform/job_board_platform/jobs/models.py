from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import User

class Job(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    company_name = models.CharField(max_length=200)
    location = models.CharField(max_length=100)
    posted_date = models.DateTimeField(auto_now_add=True)
    deadline = models.DateField()

    def __str__(self):
        return self.title

class Candidate(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    resume = models.FileField(upload_to='resumes/', blank=True)

    def __str__(self):
        return self.user.username

class Application(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    date_applied = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[
        ('applied', 'Applied'),
        ('under_review', 'Under Review'),
        ('rejected', 'Rejected'),
        ('hired', 'Hired'),
    ], default='applied')

    def __str__(self):
        return f"{self.candidate.user.username} - {self.job.title}"
