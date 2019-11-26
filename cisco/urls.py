from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('dj/', include('dj.urls')),
    path('admin/', admin.site.urls),
]
