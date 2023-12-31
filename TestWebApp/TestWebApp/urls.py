from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('database/', include('database.urls')),
    path('chat/', include('chat.urls')),
    path('game/', include('game.urls')),
    path('riot_api/', include('riot_api.urls')),
]

