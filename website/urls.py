from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('projects/', views.ProjectView.as_view(), name='projects'),
    path('organisations/', views.OrganisationView.as_view(), name='organisations'),
    path('contact/', views.contact, name='contact'),
]