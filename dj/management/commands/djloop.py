from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone

from dj.models import Song, Vote
from dj.queue import get_most_voted_song, get_current_song
from dj.templatetags.utils import elapsed_since

class Command(BaseCommand):
    help = 'Update the DJ loop'

    def handle(self, *args, **options):
        song = get_current_song()
        if song is None or (elapsed_since(song.start_time) >= song.duration):
            # Reset song
            if song:
                song.is_playing = False
                song.save()

            # Find and start next song
            new_song = get_most_voted_song()
            if not new_song:
                raise CommandError('No available song')
            new_song.is_playing = True
            new_song.start_time = timezone.now()
            new_song.save()

            # Reset votes
            votes = Vote.objects.filter(song=new_song)
            votes.delete()

            self.stdout.write(f'Playing {new_song.title}')
