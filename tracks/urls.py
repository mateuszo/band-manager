from django.conf.urls import url

from . import views

app_name = 'tracks'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^events$', views.events, name='events'),
    url(r'^events/(?P<event_id>[0-9]+)$', views.event_details, name='event_details'),
    url(r'^projects$', views.projects, name='projects'),
    url(r'^projects/(?P<project_id>[0-9]+)$', views.project_details, name='project_details'),

]