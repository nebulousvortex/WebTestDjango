from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
class Messages(models.Model):
    sender = models.ForeignKey(User, on_delete=models.PROTECT, null=True, related_name='sent_messages')
    target = models.ForeignKey(User, on_delete=models.PROTECT, null=True, related_name='received_messages')
    message = models.TextField('Сообщение')
    date = models.DateTimeField('Дата', auto_now_add=True)
