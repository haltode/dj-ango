from dj.models import Song
from dj.templatetags.utils import sort_songs_by_vote


def get_current_song():
    song = Song.objects.filter(is_playing=True).first()
    return song

def get_most_voted_song():
    songs = Song.objects.all()
    if not songs:
        return None

    sorted_songs = sort_songs_by_vote(songs)
    return sorted_songs[0]
