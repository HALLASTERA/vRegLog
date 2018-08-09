from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    post = models.CharField(models.URLField,max_length=1000)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

