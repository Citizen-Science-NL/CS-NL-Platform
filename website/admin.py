from django.contrib import admin
from .models import Hero, Highlight, Centeredsection, Newssection, ProjectPage, OrganisationPage

# Register your models here.
admin.site.register(Hero)
admin.site.register(Highlight)
admin.site.register(Centeredsection)
admin.site.register(Newssection)
admin.site.register(ProjectPage)
admin.site.register(OrganisationPage)