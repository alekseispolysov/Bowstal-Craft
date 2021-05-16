from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from . models import *

# index view

class ChatIndex(LoginRequiredMixin, generic.ListView):
	template_name = 'chat/chat_main.html'
	model = ChatWith# not model yet

	def get_queryset(self):
		user = self.request.user
		# filter everyone, who has second user assigned to it
		qs = ChatWith.objects.all().filter(user_second=user)
		print(qs)
		return qs

	# def get_context_data(self, **kwargs):
	# 	ctx = super().get_context_data(**kwargs)
	# 	ctx['myFilter'] = self.myFilter
	# 	return ctx


class ChatIndexChat(LoginRequiredMixin, generic.ListView):
	template_name = 'chat/chat_with.html'
	model = ChatWith




# Create your views here.








