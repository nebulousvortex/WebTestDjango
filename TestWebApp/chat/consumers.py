from django.contrib.auth import get_user_model
from .models import Messages
import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from django.core.exceptions import ValidationError

import time
import datetime
import logging

User = get_user_model()

logger = logging.getLogger('websocket_time')

class ChatConsumer(WebsocketConsumer):
    def connect(self):

        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        logger.info(f"[{now}] WebSocket CONNECT {self.scope['path']}")

        self.room_group_name = 'test'
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    def receive(self, text_data):

        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        logger.info(f"[{now}] WebSocket receive text_data {self.scope['path']} - {text_data}")

        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        if message and not message.isspace():
            user = self.scope.get('user')
            username = user.username if user and user.is_authenticated else 'Anonymous'

            # Сохранение сообщения в базу данных
            Messages.objects.create(sender=user, target=None, message=message)

            async_to_sync(self.channel_layer.group_send)(
                self.room_group_name,
                {
                    'type': 'chat_message',
                    'message': message,
                    'user': username
                }
            )
        else:
            raise ValidationError('Empty message')

    def chat_message(self, event):

        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        logger.info(f"[{now}] WebSocket DISCONNECT {self.scope['path']}")

        message = event['message']
        user = event['user']  # получить имя пользователя
        self.send(text_data=json.dumps({
            'type': 'chat',
            'message': message,
            'user': user  # передать имя пользователя клиенту
        }))
