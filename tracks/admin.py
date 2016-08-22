from django.contrib import admin
from .models import Event, Project, Track

# Register your models here.
admin.site.register(Event)
admin.site.register(Project)
admin.site.register(Track)