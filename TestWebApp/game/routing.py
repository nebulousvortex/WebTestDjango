from django.urls import re_path, path
from . import consumers


websocket_urlpatterns = [
    path(r'ws/game-socket/', consumers.GameConsumer.as_asgi()),
]