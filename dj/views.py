from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from . import api
from dj.models import Song, Like


def player(request):
    return render(request, 'dj/player.html')

def queue(request):
    songs = Song.objects.all()
    context = {'songs': songs}
    return render(request, 'dj/queue.html', context)

@login_required
def suggest(request):
    if request.method == 'GET':
        return render(request, 'dj/suggest.html')
    elif request.method == 'POST':
        yt_url = request.POST['yt_url']
        api.add_song(request, yt_url)
        return redirect('dj:suggest')

@login_required
def mysongs(request):
    mines = Song.objects.filter(suggester=request.user)
    likes_ids = Like.objects.filter(user=request.user) \
                    .exclude(song__in=mines).values('song')
    likes = Song.objects.filter(pk__in=likes_ids)
    context = {
        'mines': mines,
        'likes': likes,
    }
    return render(request, 'dj/mysongs.html', context)
