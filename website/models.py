from django.db import models
from django.contrib.auth.models import User



class Contents(models.Model):
    title = models.CharField(max_length=250)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    class Meta:
        abstract = True

class Hero(Contents):
    title = models.TextField()
    subtitle = models.TextField()
    buttonprimarytext = models.CharField(max_length=255)
    buttonprimaryurl = models.CharField(max_length=255)
    buttonsecondarytext = models.CharField(max_length=255)
    buttonsecondaryurl = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

class Centeredsection(Contents):
    title = models.CharField(max_length=255)
    body = models.TextField()
    buttonprimarytext = models.CharField(max_length=255)
    buttonprimaryurl = models.CharField(max_length=255)
    buttonsecondarytext = models.CharField(max_length=255)
    buttonsecondaryurl = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

class OrganisationPage(Contents):
    body = models.TextField()
    title = models.CharField(max_length=250)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

class ProjectPage(Contents):
    body = models.TextField()
    title = models.CharField(max_length=250)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
class Newssection(Contents):
    title_section1 = models.CharField(max_length=255)
    subtitle_section1 = models.CharField(max_length=255)
    body_section1 = models.TextField()
    buttonprimarytext_section1 = models.CharField(max_length=255)
    buttonprimaryurl_section1 = models.CharField(max_length=255)
    imageurl_section1 = models.CharField(max_length=255)
    title_section2 = models.CharField(max_length=255)
    subtitle_section2 = models.CharField(max_length=255)
    body_section2 = models.TextField()
    buttonprimarytext_section2 = models.CharField(max_length=255)
    buttonprimaryurl_section2 = models.CharField(max_length=255)
    imageurl_section2 = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title_section1 + ' | ' + self.author.username

class Highlight(Contents):
    title = models.TextField()
    subtitle = models.TextField()
    buttontext = models.CharField(max_length=255)
    buttonurl = models.CharField(max_length=255)
    imageurl = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title + ' | ' + self.author.username
    