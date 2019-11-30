from dj.models import Song, Vote
from dj.templatetags.utils import elapsed_since, sort_songs_by_vote
from django.utils import timezone


def get_current_song():
    song = Song.objects.filter(is_playing=True).first()
    # Check if song update
    if song is None or (elapsed_since(song.start_time) >= song.duration):
        if song:
            # Reset current song
            song.is_playing = False
            song.save()

        # Find and start next song
        new_song = get_most_voted_song()
        if new_song:
            new_song.is_playing = True
            new_song.start_time = timezone.now()
            new_song.save()

            votes = Vote.objects.filter(song=new_song)
            votes.delete()
        return new_song
    return song

def get_most_voted_song():
    songs = Song.objects.all()
    if not songs:
        return None

    sorted_songs = sort_songs_by_vote(songs)
    return sorted_songs[0]
