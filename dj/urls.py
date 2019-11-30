from django.urls import path

from . import api
from . import views

app_name = 'dj'
urlpatterns = [
    path('', views.player, name='player'),
    path('queue/', views.queue, name='queue'),
    path('suggest/', views.suggest, name='suggest'),
    path('mysongs/', views.mysongs, name='mysongs'),
    path('api/vote/<str:yt_id>/', api.vote, name='vote'),
    path('api/like/<str:yt_id>/', api.like, name='like'),
    path('api/get_song/<str:yt_id>/', api.get_song, name='get_song'),
    path('api/add_song/<str:yt_id>/', api.add_song, name='add_song'),
    path('api/state/', api.state, name='state'),
]
