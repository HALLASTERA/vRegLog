from django.db import models

from django.contrib.auth.models import User

class Post1(models.Model):
    post = models.CharField(max_length=1000)
    post1 = models.TextField(max_length=1000)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, )

