from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.core.exceptions import ValidationError
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_POST, require_GET

from . import youtube
from dj.models import Song, Vote, Like
from dj.queue import get_current_song
from dj.templatetags.utils import get_nb_votes, elapsed_since


@login_required
@require_POST
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
@require_POST
def like(request, yt_id):
    song = get_object_or_404(Song, yt_id=yt_id)
    like, created = Like.objects.get_or_create(song=song, user=request.user)
    # Liking twice undoes the first like
    if not created:
        like.delete()
    else:
        like.save()

    res = {'is_liked': created}
    return JsonResponse(res)

@require_GET
def get_song(request, yt_id):
    song = get_object_or_404(Song, yt_id=yt_id)
    serialized = serializers.serialize('json', [ song, ])
    return JsonResponse(serialized, safe=False)

@login_required
@require_POST
def add_song(request, yt_url):
    yt_id = youtube.extract_video_id(yt_url)
    meta = youtube.get_video_metadata(yt_id)
    if not meta:
        err = f'Invalid video id: {yt_id}'
        messages.error(request, err)
        return JsonResponse({'type': 'error', 'text': err})
    else:
        song = Song(
            title=meta['title'],
            author=meta['author'],
            duration=meta['duration'],
            yt_id=yt_id,
            suggester=request.user
        )
        try:
            song.full_clean()
            song.save()
            suc = f'Song {song.title} was added.'
            messages.success(request, suc)
            return JsonResponse({'type': 'success', 'text': suc})
        except ValidationError as err:
            err = '; '.join(err.messages)
            messages.error(request, err)
            return JsonResponse({'type': 'error', 'text': err})

@require_GET
def state(request):
    song = get_current_song()
    if not song:
        return JsonResponse({})
    else:
        res = {
            'yt_id': song.yt_id,
            'elapsed': elapsed_since(song.start_time).total_seconds(),
        }
        return JsonResponse(res)
