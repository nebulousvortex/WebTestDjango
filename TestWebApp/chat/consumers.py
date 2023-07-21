from django.contrib.auth import get_user_model
from .models import Messages
import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from django.core.exceptions import ValidationError

User = get_user_model()


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_group_name = 'test'
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    def receive(self, text_data):
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
        message = event['message']
        user = event['user']  # получить имя пользователя
        self.send(text_data=json.dumps({
            'type': 'chat',
            'message': message,
            'user': user  # передать имя пользователя клиенту
        }))
