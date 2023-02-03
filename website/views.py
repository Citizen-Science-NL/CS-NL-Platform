from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, TemplateView, View
from .models import Hero, Highlight, Centeredsection, Newssection, ProjectPage, OrganisationPage
import requests

def get_data(kind):
        r = requests.get("https://eu-citizen.science/api/"+kind+"?country=NL")
        content = r.json()
        return content
    

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

#def home(request):
 #   return render(request, 'home_page.html', {} )

def organisations(request):
    return render(request, 'organisations_page.html', {} )

def projects(request):
    return render(request, 'project_page.html', {} )

def contact(request):
    return render(request, 'contact_page.html', {} )

class HomeView(TemplateView):
    template_name = 'home_page.html'
    
    def get_context_data(self, **kwargs):
         context = super(HomeView, self).get_context_data(**kwargs)
         context['Hero'] = Hero.objects.all()
         context['Highlight'] = Highlight.objects.all()
         context['Centeredsection'] = Centeredsection.objects.all()
         context['Newssection'] = Newssection.objects.all()
         return context

class ProjectView(TemplateView):
    template_name = 'project_page.html'
    
    def get_context_data(self, **kwargs):
         context = super(ProjectView, self).get_context_data(**kwargs)
         context['project_page'] = ProjectPage.objects.all()
         context['projectlist'] = get_data('projects')
         return context
     
class OrganisationView(TemplateView):
    template_name = 'organisations_page.html'
    
    def get_context_data(self, **kwargs):
         context = super(OrganisationView, self).get_context_data(**kwargs)
         context['organisation_page'] = OrganisationPage.objects.all()
         context['organisationlist'] = get_data('organisations')
         return context