from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Room(models.Model):
    """
    Model room of chat
    """
    class Meta:
        verbose_name = 'Комната чата'
        verbose_name_plural = 'Комнаты чата'

    creator = models.ForeignKey(User, verbose_name='Создатель', on_delete=models.CASCADE)
    invited = models.ManyToManyField(User, verbose_name='Учасники', related_name='invited_user')
    date = models.DateTimeField('Дата создания', auto_now_add=True)


class Chat(models.Model):
    """
    Chat model
    """
    class Meta:
        verbose_name = 'Сообщение чата'
        verbose_name_plural = 'Сообщения чатов'

    room = models.ForeignKey(Room, verbose_name='Комната чата', on_delete=models.CASCADE)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    text = models.TextField('Сообщения', max_length=500)
    date = models.DateTimeField('Дата отправки', auto_now_add=True)
