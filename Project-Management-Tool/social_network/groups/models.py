from django.db import models

# Create your models here.

# groups/models.py

from django.db import models
from users.models import User

class Group(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    members = models.ManyToManyField(User, related_name='groups')

    def __str__(self):
        return self.name
