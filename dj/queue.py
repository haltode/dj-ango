from dj.models import Song
from dj.templatetags.utils import get_nb_votes


def get_current_song():
    song = Song.objects.filter(is_playing=True).first()
    return song

def get_songs_sorted_by_vote():
    songs = Song.objects.all()
    sorted_songs = sorted(songs, key=lambda s: get_nb_votes(s), reverse=True)
    return sorted_songs

def get_most_voted_song():
    songs = get_songs_sorted_by_vote()
    if songs:
        return songs[0]
    else:
        return None
