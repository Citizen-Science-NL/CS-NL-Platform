from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, TemplateView
from .models import Hero, Highlight

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
         return context
