from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Hero(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    linkprimary = models.CharField(max_length=255)
    linksecondary = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title + ' | ' + self.author