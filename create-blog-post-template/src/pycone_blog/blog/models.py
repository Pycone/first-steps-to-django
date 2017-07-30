from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    post_url = models.CharField(max_length=100)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
