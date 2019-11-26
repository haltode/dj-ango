from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('dj/', include('dj.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('social_django.urls', namespace='social')),
]
