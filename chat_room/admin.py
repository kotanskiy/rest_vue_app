from django.contrib import admin

# Register your models here.
from chat_room.models import Room, Chat


class RoomAdmin(admin.ModelAdmin):
    """
    Chat rooms
    """
    list_display = (
        'creator',
        'invited_user',
        'date'
    )

    def invited_user(self, obj):
        return '\n'.join([user.username for user in obj.invited.all()])


class ChatAdmin(admin.ModelAdmin):
    """
    Chat dialogs
    """
    list_display = (
        'room',
        'user',
        'text',
        'date'
    )


admin.site.register(Chat, ChatAdmin)
admin.site.register(Room, RoomAdmin)
