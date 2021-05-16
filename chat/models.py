from django.db import models
from django.contrib.auth.models import User

# Create your models here.




class ChatWith(models.Model):
	user_qs = models.ForeignKey(User, related_name="user_qs_table", blank=True, null=True, on_delete=models.CASCADE)
	user_second = models.ForeignKey(User, related_name="user_second_table", blank=True, null=True, on_delete=models.CASCADE)




