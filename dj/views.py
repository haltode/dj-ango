from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import Song, Vote


def player(request):
    return render(request, 'dj/player.html')

def queue(request):
    songs = Song.objects.all()
    context = {'songs': songs}
    return render(request, 'dj/queue.html', context)

def song(request, yt_id):
    song = get_object_or_404(Song, yt_id=yt_id)
    context = {'song': song}
    return render(request, 'dj/song.html', context)

@login_required
def vote(request, yt_id):
    song = get_object_or_404(Song, yt_id=yt_id)
    vote, created = Vote.objects.get_or_create(song=song, user=request.user)
    # Voting twice undoes the first vote
    if not created:
        vote.delete()
        return HttpResponse('Unvote successful')
    else:
        vote.save()
        return HttpResponse('Vote successful')
