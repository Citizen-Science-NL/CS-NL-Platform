from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('projects/', views.ProjectView.as_view(), name='projects'),
    path('organisations/', views.OrganisationView.as_view(), name='organisations'),
    path('contact/', views.contact, name='contact'),
    path('edithero/<int:pk>/', views.UpdateHeroView.as_view(), name='edithero'),
    path('edithighlight/<int:pk>/', views.UpdateHighlight.as_view(), name='edithighlight'),
    path('editcenteredsection/<int:pk>/', views.UpdateCenteredsection.as_view(), name='editcenteredsection'),
    path('editnewssection/<int:pk>/', views.UpdateNewssection.as_view(), name='editnewssection'),
    path('editprojects/<int:pk>/', views.UpdateProjects.as_view(), name='editprojects'),
    path('editorganisations/<int:pk>/', views.UpdateOrganisation.as_view(), name='editorganisations'),
]
