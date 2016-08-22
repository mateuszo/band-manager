from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Track, Project, Event
import datetime

# Create your views here.
def index(request):
    week_ago = datetime.date.today() - datetime.timedelta(days=7)
    tracks = Track.objects.filter(date__gte=week_ago)
    projects = Project.objects.filter(date__gte=week_ago)
    events = Event.objects.filter(date__gte=week_ago)
    return render(request, 'tracks/index.html', {'tracks': tracks,
                                                 'projects': projects,
                                                 'events': events})


def events(request):
    events = Event.objects.all()
    return render(request, 'tracks/events.html', {'events': events})


def event_details(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    return render(request, 'tracks/event_details.html', {'event': event})


def projects(request):
    projects = Project.objects.all()
    return render(request, 'tracks/projects.html', {'projects': projects})


def project_details(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    return render(request, 'tracks/project_details.html', {'project': project})
