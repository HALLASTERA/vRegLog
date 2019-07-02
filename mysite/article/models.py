from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class ModelArticle(models.Model):
    title = models.TextField()
    bodytext = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, models.SET_NULL, null=True)



STATUS_CHOICES = (
    ('d', 'Draft'),
    ('p', 'Published'),
    ('w', 'Withdrawn'),
)
class Article(models.Model):
    title1 = models.CharField(max_length=100)
    body = models.TextField()
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    headshot = models.ImageField(null=True, blank=True, upload_to="hero_headshots/")

    def __str__(self):
        return self.title1