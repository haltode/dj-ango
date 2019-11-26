from django import template

from dj.models import Vote

register = template.Library()


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
