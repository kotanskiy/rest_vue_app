from django.contrib.auth.models import User
from rest_framework import serializers
from chat_room.models import Room, Chat


class UserSerializer(serializers.ModelSerializer):
    """
    User serializer
    """
    class Meta:
        model = User
        fields = (
            'id',
            'username'
        )


class RoomSerializer(serializers.ModelSerializer):
    """
    Model serializer chat rooms
    """

    class Meta:
        model = Room
        fields = (
            'creator',
            'invited',
            'date'
        )

    creator = UserSerializer()
    invited = UserSerializer(many=True)


class ChatSerializer(serializers.ModelSerializer):
    """
    Chat serializer
    """

    class Meta:
        model = Chat
        fields = (
            'user',
            'date',
            'text'
        )
