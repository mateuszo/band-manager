from django.db import models
from datetime import date

class Event(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    date = models.DateField(default=date.today())

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateField(default=date.today())
    description = models.TextField(blank=True)
    # TODO: add state field definig the project's state (done/in progress)

    def __str__(self):
        return self.name


class Track(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateField(default=date.today())
    path = models.CharField(max_length=500)
    event = models.ForeignKey(Event)
    project = models.ForeignKey(Project, blank=True, null=True)

    def __str__(self):
        return self.name
