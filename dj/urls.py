from django.urls import path

from . import views

app_name = 'dj'
urlpatterns = [
    path('queue/', views.queue, name='queue'),
    path('song/<str:yt_id>/', views.song, name='song'),
    path('vote/<str:yt_id>/', views.vote, name='vote'),
]
