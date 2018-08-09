from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class ModelArticle(models.Model):
    title = models.TextField()
    bodytext = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, models.SET_NULL, null=True)