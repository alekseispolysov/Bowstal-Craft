from django.db import models
from django.contrib.auth.models import User

from forum.models import ForumPost

# quick fix to user model, without writing in it

# email must be unique, required and if it is already in db no blow up
User._meta.get_field('email')._unique = True
User._meta.get_field('email').blank = False
User._meta.get_field('email').null = True


# User profile model, not good solution but ok for now

class User_Profile(models.Model):
	# add options of gender -> male or female
	GENDER = (
		('Male', 'Male'),
		('Female', 'Female'),
		('Other', 'Other'),	
		)

	user = models.OneToOneField(User, related_name="user_profile", blank=True, null=True, on_delete=models.CASCADE)
	
	date_of_birth = models.DateField(blank=True, null=True)

	gender = models.CharField(max_length=15, null=True, blank=True, choices=GENDER)

	profile_picture = models.ImageField(default="user_default_images/default_user_picture.png", null=True, blank=True)

	description = models.TextField(max_length=450, null=True, blank=True)


	# change reputation to the int field (change datatype + apply reputation schema)
	reputation = models.CharField(default="0",max_length=30, null=True, blank=True)

	opinion_posts = models.ManyToManyField(ForumPost, blank=True)


	def __str__(self):
		try:
			return self.user.username
		except:
			print('Something went wrong, while loading user.username, probably, because something missing in database')
			return 'Err'





#class UserProfile(models.Model):


