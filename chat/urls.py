from django.urls import path

from . views import *

appname = 'chat'

urlpatterns = [
# std chat url
path('', ChatIndex.as_view(), name='chat-index'),
path('<str:pk>/', ChatIndexChat.as_view(), name='chat-with-others'),
# chat url to chat with another user
#path('/<str:name>/', , name='chat-direct'),
]