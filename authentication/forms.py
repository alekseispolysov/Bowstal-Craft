from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from . models import *


class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

	def __init__(self, *args, **kwargs):
		super(CreateUserForm, self).__init__(*args, **kwargs)

		for fieldname in ['username', 'password1', 'password2']:
			self.fields[fieldname].help_text = None


# class UpdateProfileForm(ModelForm):
# 	class Meta:
# 		model = User_Profile
# 		#fields = '__all__'
# # 		exclude = ['user']
class AuthenticationForm(AuthenticationForm):
	class Meta:
		model = User
		fields = ('email', 'password')
		# username = forms.CharField(label='Email')


class UserProfileForm(ModelForm):
	class Meta:
		model = User
		# fields = '__all__'
		fields = ['username', 'first_name', 'last_name']
		# exclude = ['email', 'password', 'groups', 'user_permissions', 'is_staff', 'is_active', 'is_superuser', 'last_login', 'date_joined']


class ProfileUserForm(ModelForm):
	# username = forms.CharField(label='Your Username (Nickname)', max_length=100)

	class Meta:
		model = User_Profile
		fields = '__all__'
		exclude = ['user', 'reputation', 'opinion_posts']

	
	# вытащить всё что нужно из user модели, использовать уже готовую модель user_profile

	# что я могу хранить в user model?
	# username, firstname, lastname, email, is_staff, is_super, date_joined
	# I need create gender, date of birth in user_profile model

	# name = forms.CharField(label='Your name', max_length=100)
	# lastname = forms.CharField(label='Your lastname', max_length=100)
	# date_of_birth = forms.CharField(label='Your lastname', max_length=100)
	# gender = forms.CharField(label='Gender', max_length=100)
	# profile_pic = models.ImageField(default="profile_thing.png", null=True, blank=True)





# class AuthenticationForm(AuthenticationForm):

#     class Meta:
#         model = User
#         fields = '__all__'

#     def __init__(self, *args, **kwargs):
#         super(AuthenticationForm, self).__init__(*args, **kwargs)

#         for field in self.fields.values():
#             field.error_messages = {'required':'{fieldname} is required'.format(
#             fieldname=field.label)}