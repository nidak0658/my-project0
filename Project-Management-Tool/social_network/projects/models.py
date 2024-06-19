from django.db import models

# Create your models here.

# projects/models.py

from django.db import models
from groups.models import Group

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='projects')

    def __str__(self):
        return self.title
