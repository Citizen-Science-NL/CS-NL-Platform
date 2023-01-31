from django.db import models
import requests


# New imports added for ParentalKey, Orderable, InlinePanel

from modelcluster.fields import ParentalKey
from wagtail.models import Page, Orderable
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, InlinePanel
from wagtail.search import index


class HomePage(Page):
    date = models.DateField("Post date")
    intro = models.CharField(max_length=250)
    bodyheading = models.CharField(max_length=250)
    bodytext = RichTextField(blank=True)
    headingoneheading = models.CharField(max_length=250)
    headingonetext = models.CharField(max_length=250)
    headingtwoheading = models.CharField(max_length=250)
    headingtwotext = models.CharField(max_length=250)
    headingthreeheading = models.CharField(max_length=250)
    headingthreetext = models.CharField(max_length=250)


    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('bodytext'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('date'),
        FieldPanel('intro'),
        FieldPanel('bodyheading'),
        FieldPanel('bodytext'),
        FieldPanel('headingoneheading'),
        FieldPanel('headingonetext'),
        FieldPanel('headingtwoheading'),
        FieldPanel('headingtwotext'),
        FieldPanel('headingthreeheading'),
        FieldPanel('headingthreetext'),    
    ]

class ContentPage(Page):
    body = RichTextField(blank=True)
    hero = RichTextField(blank=True)
    intro = models.CharField(max_length=250)
    
    @property
    def get_projects(self):
        r = requests.get("https://eu-citizen.science/api/projects?country=NL")
        projects = r.json()
        return projects
    

    content_panels = Page.content_panels + [
        FieldPanel('body'),
        FieldPanel('hero'),
        FieldPanel('intro'),
        InlinePanel('gallery_images', label="Gallery images"),
    ]
    
class ProjectPage(Page):
    body = RichTextField(blank=True)
    hero = RichTextField(blank=True)
    intro = models.CharField(max_length=250)
    
    @property
    def get_projects(self):
        r = requests.get("https://eu-citizen.science/api/projects?country=NL")
        projects = r.json()
        return projects
    

    content_panels = Page.content_panels + [
        FieldPanel('body'),
        FieldPanel('hero'),
        FieldPanel('intro'),
    ]
    
class OrganisationsPage(Page):
    body = RichTextField(blank=True)
    hero = RichTextField(blank=True)
    intro = models.CharField(max_length=250)
    
    @property
    def get_organisations(self):
        r = requests.get("https://eu-citizen.science/api/organisations?country=NL")
        organisations = r.json()
        return organisations
    

    content_panels = Page.content_panels + [
        FieldPanel('body'),
        FieldPanel('hero'),
        FieldPanel('intro'),
    ]

class GalleryImage(Orderable):
    page = ParentalKey(ContentPage, on_delete=models.CASCADE, related_name='gallery_images')
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    )
    caption = models.CharField(blank=True, max_length=250)

    panels = [
        FieldPanel('image'),
        FieldPanel('caption'),
    ]

class ContactPage(Page):
    body = RichTextField(blank=True)
    hero = RichTextField(blank=True)
    intro = models.CharField(max_length=250)
    

    content_panels = Page.content_panels + [
        FieldPanel('body'),
        FieldPanel('hero'),
        FieldPanel('intro'),
    ]
    