from django import template
from django.utils import timezone

from dj.models import Vote, Like

from datetime import timedelta

register = template.Library()


@register.filter
def elapsed_since(start):
    end = timezone.now()
    delta = (end - start).total_seconds()
    return timedelta(seconds=int(delta))

@register.filter
def format_duration(duration):
    total_seconds = int(duration.total_seconds())
    hours, remainder = divmod(total_seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    if hours > 0:
        return f'{hours}:{minutes}:{seconds}'
    else:
        return f'{minutes}:{seconds}'

@register.filter
def sort_songs_by_vote(songs):
    sorted_songs = sorted(songs, key=lambda s: get_nb_votes(s), reverse=True)
    return sorted_songs

@register.simple_tag
def get_nb_votes(song):
    votes = Vote.objects.filter(song=song)
    return len(votes)

@register.simple_tag
def has_vote(song, user):
    try:
        Vote.objects.get(song=song, user=user)
        return True
    except Vote.DoesNotExist:
        return False

@register.simple_tag
def has_like(song, user):
    try:
        Like.objects.get(song=song, user=user)
        return True
    except Like.DoesNotExist:
        return False
