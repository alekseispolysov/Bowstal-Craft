from django.shortcuts import render, redirect
from django.views import View
from django.views.generic.edit import FormView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.contrib import messages #import messages

from . models import *
from . forms import *


register_template = 'authentication/registration.html'

class RegistrationPage(View):
	def get(self, request):
		if request.user.is_authenticated:
			return redirect('mainapp:home-page')
		# text = request.GET.get('button_text')

		# print()
		# print(text)
		# print()

		form = CreateUserForm()
		ctx = {
		'form':form,
		}

		return render(request, register_template, ctx)
	def post(self, request):
		form = CreateUserForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password1')
			user_auth = authenticate(username=username, password=password)
			login(request, user_auth)
			# all after form login defined in signals
			
			return redirect('mainapp:home-page')
			#messages.success(request, 'Account was created for ' + username)
		else:
			#not refresh the form, because otherwise errors won't be returned
			la = 'hello world'
			ctx = {
			'form':form,
			'hi':la,
			}
			return render(request, register_template, ctx)


class UserProfile(LoginRequiredMixin, View):
	def get(self, request):
		user = User.objects.get(pk=request.user.id)
		ctx = {
		'user':user,
		}
		return render(request, 'authentication/user_profile.html', ctx)


class ViewProfilePage(View):
	def get(self, request, pk):
		user_object = User.objects.get(pk=pk)
		ctx={
		'user_object':user_object,
		}
		return render(request, 'authentication/user_profile_view.html', ctx)