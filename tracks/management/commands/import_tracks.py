from django.core.management.base import BaseCommand, CommandError
from tracks.models import Track, Event
from dateutil import parser
import os

class Command(BaseCommand):
    help = 'Import event folder with tracks'

    def add_arguments(self, parser):
        parser.add_argument('dir_name', nargs='+', type=str)

    def handle(self, *args, **options):
        for dir in options['dir_name']:
            print("Importing", dir)
            event = Event()
            event.name = 'Próba ' + dir
            event.date = parser.parse(dir)
            event.save()
            track_names = os.listdir('tracks/static/audio/' + dir)
            for track_name in track_names:
                track = Track()
                track.name = track_name
                track.path = dir + '/' + track_name
                track.date = event.date
                track.event = event
                track.save()

