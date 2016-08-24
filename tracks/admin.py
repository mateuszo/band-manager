from django.contrib import admin
from .models import Event, Project, Track


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'status')
    list_editable = ('status',)
    # list_display_links = 'name'


# Register your models here.
admin.site.register(Event)
# admin.site.register(Project)
admin.site.register(Track)

