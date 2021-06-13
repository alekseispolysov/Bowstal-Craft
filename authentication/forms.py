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


# class AuthenticationForm(AuthenticationForm):

#     class Meta:
#         model = User
#         fields = '__all__'

#     def __init__(self, *args, **kwargs):
#         super(AuthenticationForm, self).__init__(*args, **kwargs)

#         for field in self.fields.values():
#             field.error_messages = {'required':'{fieldname} is required'.format(
#             fieldname=field.label)}