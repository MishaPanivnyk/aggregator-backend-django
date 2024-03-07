from django.db import models
from datetime import datetime


# Create your models here.
class Blog(models.Model):

    title = models.CharField(max_length=60)
    content = models.TextField()
    author = models.CharField(max_length=30)
    category = models.CharField(max_length=30)
    time_create = models.DateTimeField(default=datetime.now())

