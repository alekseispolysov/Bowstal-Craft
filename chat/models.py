from django.db import models
from django.contrib.auth.models import User

# Create your models here.




class ChatWith(models.Model):
	user_qs = models.ForeignKey(User, related_name="user_qs_table", blank=True, null=True, on_delete=models.CASCADE)
	user_second = models.ForeignKey(User, related_name="user_second_table", blank=True, null=True, on_delete=models.CASCADE)



# the logic is this
# user creates message to somebody
# then somebody get permission to use this id of chat
# then he recieves the message and can reply
# if he don't want to chat with, he can set permission to the other user, so other user cannot even write and this user, cannot see what the other user is typed, all messages got deleted
class Chat(models.Model):
	pass

class Chat_line(models.Model):
	user = models.ForeignKey(User, related_name="user", blank=True, null=True, on_delete=models.CASCADE)
	chat = models.ForeignKey(Chat, related_name="chat", blank=True, null=True, on_delete=models.CASCADE)
	content = models.CharField(max_length=50, null=True)
	date_sent = models.DateTimeField(auto_now_add=True, null=True)
