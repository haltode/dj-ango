from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render, redirect

from .models import Song, Vote
from .templatetags.utils import get_nb_votes

import requests


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

def mysongs(request):
    return render(request, 'dj/mysongs.html')

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

@login_required
def suggest(request):
    def get_metadata(yt_id):
        url = 'https://www.googleapis.com/youtube/v3/videos'
        params = {
            'id': yt_id,
            'part': 'contentDetails,snippet',
            'key': settings.YOUTUBE_API_KEY,
        }
        req = requests.get(url=url, params=params)

        json = req.json()['items'][0]
        meta = {
            'title': json['snippet']['title'],
            'author': json['snippet']['channelTitle'],
            'duration': json['contentDetails']['duration'],
        }
        return meta

    # The video id is stored in the HTML form
    yt_id = request.POST['yt_id']
    meta = get_metadata(yt_id)
    # TODO: check for error
    song = Song(
        title=meta['title'],
        author=meta['author'],
        duration=meta['duration'],
        yt_id=yt_id,
        suggester=request.user
    )
    song.save()
    return redirect('dj:queue')
