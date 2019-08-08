from django.contrib import admin
from django.urls import path
from chat_room.views import *


urlpatterns = [
    path('room/', RoomView.as_view()),
    path('dialog/', DialogView.as_view())
]
