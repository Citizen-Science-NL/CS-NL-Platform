from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from .models import Hero

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

class HomeView(ListView):
    model = Hero
    template_name = 'home_page.html'