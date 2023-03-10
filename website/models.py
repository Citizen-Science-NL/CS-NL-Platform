from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField


# Create your models here.
class Hero(models.Model):
    title = models.TextField()
    #subtitle = models.TextField()
    subtitle = RichTextField(blank=True, null=True)
    buttonprimarytext = models.CharField(max_length=255)
    buttonprimaryurl = models.CharField(max_length=255)
    buttonsecondarytext = models.CharField(max_length=255)
    buttonsecondaryurl = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title + ' | ' + self.author.username
    
    def get_absolute_url(self): # new
        return reverse('home')
    
class Highlight(models.Model):
    title = models.TextField()
    subtitle = subtitle = RichTextField(blank=True, null=True)
    buttontext = models.CharField(max_length=255)
    buttonurl = models.CharField(max_length=255)
    imageurl = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title + ' | ' + self.author.username
    def get_absolute_url(self): # new
        return reverse('home')
    
class Centeredsection(models.Model):
    title = models.CharField(max_length=255)
    body = RichTextField(blank=True, null=True)
    buttonprimarytext = models.CharField(max_length=255)
    buttonprimaryurl = models.CharField(max_length=255)
    buttonsecondarytext = models.CharField(max_length=255)
    buttonsecondaryurl = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title + ' | ' + self.author.username
    def get_absolute_url(self): # new
        return reverse('home')
    
    
class Newssection(models.Model):
    title_section1 = models.CharField(max_length=255)
    subtitle_section1 = models.CharField(max_length=255)
    body_section1 = RichTextField(blank=True, null=True)
    buttonprimarytext_section1 = models.CharField(max_length=255)
    buttonprimaryurl_section1 = models.CharField(max_length=255)
    imageurl_section1 = models.CharField(max_length=255)
    title_section2 = models.CharField(max_length=255)
    subtitle_section2 = models.CharField(max_length=255)
    body_section2 = RichTextField(blank=True, null=True)
    buttonprimarytext_section2 = models.CharField(max_length=255)
    buttonprimaryurl_section2 = models.CharField(max_length=255)
    imageurl_section2 = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title_section1 + ' | ' + self.author.username
    def get_absolute_url(self): # new
        return reverse('home')
    
class ProjectPage(models.Model):
    body = models.TextField()
    title = models.CharField(max_length=250)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    def get_absolute_url(self): # new
        return reverse('home')
    
class OrganisationPage(models.Model):
    body = models.TextField()
    title = models.CharField(max_length=250)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def get_absolute_url(self): # new
        return reverse('home')