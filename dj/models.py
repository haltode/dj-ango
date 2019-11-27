from django.contrib.auth.models import User
from django.db import models


class Song(models.Model):
    title = models.CharField(max_length=256)
    author = models.CharField(max_length=256)
    duration = models.DurationField()
    is_playing = models.BooleanField(default=False)
    start_time = models.DateTimeField(null=True, blank=True)

    yt_id = models.CharField(max_length=11, unique=True)
    suggester = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title} - {self.author} ({self.duration}s)'

class Vote(models.Model):
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['song', 'user'], name='unique vote')
        ]

    def __str__(self):
        return f'{self.user} voted for {self.song}'
