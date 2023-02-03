from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Hero(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    buttonprimarytext = models.CharField(max_length=255)
    buttonprimaryurl = models.CharField(max_length=255)
    buttonsecondarytext = models.CharField(max_length=255)
    buttonsecondaryurl = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title + ' | ' + self.author.username
    
class Highlight(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    buttontext = models.CharField(max_length=255)
    buttonurl = models.CharField(max_length=255)
    imageurl = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title + ' | ' + self.author.username