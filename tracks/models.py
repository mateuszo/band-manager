from django.db import models
from datetime import date
from django.utils.timezone import now


class Event(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    date = models.DateField(default=now)

    def __str__(self):
        return self.name


class Project(models.Model):
    PROJECT_STATUSES = (
        ('DRAFT', 'draft'),
        ('IN PROGRESS', 'in progress'),
        ('DONE', 'done'),
        ('OLD', 'old')
    )

    PROJECT_STATUSES_CSS = {
        "DRAFT" : 'label-warning',
        "IN PROGRESS" : 'label-info',
        "DONE" : 'label-success',
        "OLD" : 'label-default',
    }

    def get_status_css(self):
        return self.PROJECT_STATUSES_CSS[self.status]

    name = models.CharField(max_length=200)
    date = models.DateField(default=now)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=15, choices=PROJECT_STATUSES, default='DRAFT')

    def __str__(self):
        return self.name


class Track(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateField(default=now)
    path = models.CharField(max_length=500)
    event = models.ForeignKey(Event)
    project = models.ForeignKey(Project, blank=True, null=True)

    def __str__(self):
        return self.name
