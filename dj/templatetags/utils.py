from django import template
from django.utils import timezone

from dj.models import Vote

from datetime import timedelta

register = template.Library()


@register.filter
def elapsed_since(start):
    end = timezone.now()
    delta = (end - start).total_seconds()
    return timedelta(seconds=int(delta))

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
