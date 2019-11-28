from django.urls import path

from . import views

app_name = 'dj'
urlpatterns = [
    path('', views.player, name='player'),
    path('queue/', views.queue, name='queue'),
    path('mysongs/', views.mysongs, name='mysongs'),
    path('state/', views.state, name='state'),
    path('info/<str:yt_id>/', views.info, name='info'),
    path('vote/<str:yt_id>/', views.vote, name='vote'),
    path('like/<str:yt_id>/', views.like, name='like'),
    path('suggest/', views.suggest, name='suggest'),
]
