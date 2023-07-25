import random

from django.contrib.auth import get_user_model
import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from django.core.exceptions import ValidationError

User = get_user_model()


class GameObject:
    def __init__(self, player):
        self.player = player
        self.x = random.randint(50, 450)
        self.y = random.randint(50, 450)
        self.type = 'circle'

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_player(self):
        return self.player

    def get_type(self):
        return self.type


class GameConsumer(WebsocketConsumer):
    objectList = []

    def connect(self):
        self.room_group_name = 'game'
        user = self.scope.get('user')
        username = user.username if user and user.is_authenticated else 'Anonymous'
        print(username)

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name,
        )
        self.accept()


    def receive(self, text_data):
        text_data_json = json.loads(text_data)

        if text_data_json['type'] == 'move':
            async_to_sync(self.channel_layer.group_send)(
                self.room_group_name,
                {
                    'type': 'moveObject',
                    'message': text_data_json
                }
            )

        elif text_data_json['type'] == 'create':
            async_to_sync(self.channel_layer.group_send)(
                self.room_group_name,
                {
                    'type': 'createObject',
                    'message': ''
                }
            )

        elif text_data_json['type'] == 'delete':
            async_to_sync(self.channel_layer.group_send)(
                self.room_group_name,
                {
                    'type': 'delete_object',
                    'message': ''
                }
            )


    def delete_object(self, event):
        user = self.scope.get('user')
        username = user.username if user and user.is_authenticated else 'Anonymous'
        obj = self.get_data(username)
        self.objectList.remove(obj)

    def get_data(self, player):
        for obj in self.objectList:
            if obj.player == player:
                return obj

    def createObject(self, event):
        user = self.scope.get('user')
        username = user.username if user and user.is_authenticated else 'Anonymous'

        self.objectList.append(GameObject(username))
        obj = self.get_data(username)

        for newObj in self.objectList:
            self.send(text_data=json.dumps({
                'type': 'create',
                'data': {'x': newObj.get_x(), 'y': newObj.get_y(), 'type': 'circle',
                         'player': newObj.get_player()},
            }))

    def moveObject(self, event):
        action = event['message']['direction']
        user = self.scope.get('user')
        username = user.username if user and user.is_authenticated else 'Anonymous'
        obj = self.get_data(username)

        if action == 37:
            obj.x -= 5
            self.send(text_data=json.dumps({
                'type': 'movement',
                'data': {'x': obj.x, 'y': obj.y, 'player': username}
            }))
        if action == 39:
            obj.x += 5
            self.send(text_data=json.dumps({
                'type': 'movement',
                'data': {'x': obj.x, 'y': obj.y, 'player': username}
            }))
