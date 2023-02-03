from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('projects/', views.projects, name='projects'),
    path('organisations/', views.organisations, name='organisations'),
    path('contact/', views.contact, name='contact'),
]