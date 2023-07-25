from django.urls import re_path, path

from game import consumers as gameconsumers
from . import consumers


websocket_urlpatterns = [
    path(r'ws/chat-server/', consumers.ChatConsumer.as_asgi()),
    path(r'ws/game-socket/', gameconsumers.GameConsumer.as_asgi()),
]