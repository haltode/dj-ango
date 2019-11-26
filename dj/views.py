from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render

from .models import Song, Vote
from .templatetags.utils import get_nb_votes


def player(request):
    return render(request, 'dj/player.html')

def queue(request):
    songs = Song.objects.all()
    sorted_songs = sorted(songs, key=lambda s: get_nb_votes(s), reverse=True)
    context = {'songs': sorted_songs}
    return render(request, 'dj/queue.html', context)

def song(request, yt_id):
    song = get_object_or_404(Song, yt_id=yt_id)
    context = {'song': song}
    return render(request, 'dj/song.html', context)

# API only used with Ajax so it returns a JSON not HTML
@login_required
def vote(request, yt_id):
    song = get_object_or_404(Song, yt_id=yt_id)
    vote, created = Vote.objects.get_or_create(song=song, user=request.user)
    # Voting twice undoes the first vote
    if not created:
        vote.delete()
    else:
        vote.save()

    res = {
        'nb_votes': get_nb_votes(song),
        'is_upvote': created,
    }
    return JsonResponse(res)
