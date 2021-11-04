from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Tasks(models.Model):
    title = models.CharField(max_length=255)
    completed = models.BooleanField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)