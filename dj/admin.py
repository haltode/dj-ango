from django.contrib import admin

from .models import Song, Vote, Like

admin.site.register(Song)
admin.site.register(Vote)
admin.site.register(Like)
