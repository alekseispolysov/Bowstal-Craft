from django.shortcuts import render, redirect
from django.views import View, generic
from django.views.generic.edit import FormView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate, login
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.views.generic import DetailView

from itertools import chain

from . models import *
from . forms import *
from . owner import *
from . filters import *


# class ForumIndexPage(View):
# 	def get(self, request):

# 		return render(request, "forum/forum_index.html")


# protect delete and update views
class ForumIndexPage(generic.ListView):
	template_name = 'forum/forum_index.html'
	paginate_by = 20
	model = ForumPost
	def get_queryset(self):
		posts = ForumPost.objects.all()
		# filter all usernames
		queryset = super(ForumIndexPage, self).get_queryset()

		

		#qs = sorted(queryset_chain)

		self.myFilter = ForumFilter(self.request.GET, queryset=posts)
		queryset = self.myFilter.qs
		return queryset

	def get_context_data(self, **kwargs):
		ctx = super().get_context_data(**kwargs)
		ctx['myFilter'] = self.myFilter
		return ctx


# creating the new post
class CreateForumPost(LoginRequiredMixin, CreateView):
	template_name = 'forum/forum_create_post.html'
	model = ForumPost
	form_class = ForumPostForm
	success_url = reverse_lazy('forum:forum-index-page')

	def form_valid(self, form):
		form.instance.user = self.request.user
		# you can define in witch order you calling the super method
		return super().form_valid(form)

# updating the new post
class UpdateForumPost(OwnerUpdateView):
	template_name = 'forum/forum_update_post.html'
	model = ForumPost
	form_class = ForumPostForm
	success_url = reverse_lazy('forum:forum-index-page')

	def get_context_data(self, **kwargs):
		ctx = super().get_context_data(**kwargs) # run data from generic view first, then append here something else
		# going into super class
		#ctx['crazy'] = 'CRAZY THING, COMPLETLY DUM'
		return ctx

# deleting post
class DeleteForumPost(OwnerDeleteView):
	template_name = 'forum/forum_delete_post.html'
	model = ForumPost
	success_url = reverse_lazy('forum:forum-index-page')

# detail view of the post
class DetailForumPage(DetailView):
	template_name = 'forum/forum_detail_post.html'
	model = ForumPost




