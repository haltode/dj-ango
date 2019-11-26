from django.contrib import admin

from .models import Song, Vote

admin.site.register(Song)
admin.site.register(Vote)
