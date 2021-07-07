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
		# здесь прибавить important посты (если топика импортант)
		
		# print(self.important_post)
		queryset = self.myFilter.qs 
		#  [::-1] = to reverse the queryset
		return queryset[::-1]

	def get_context_data(self, **kwargs):
		ctx = super().get_context_data(**kwargs)
		ctx['myFilter'] = self.myFilter
		ctx['importantObjects'] = ForumPost.objects.all().filter(topic__icontains="Important")
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
class DetailForumPage(View):
	# template_name = 'forum/forum_detail_post.html'
	# model = ForumPost

	def getqueryrelation(self, request, post):
		# function that is taking everything that repeating in it. It is checking if user has a query relation with post. If he liked or disliked that post
		# also it checks, if user is authenticated
		if request.user.is_authenticated:
			query_relation = Reputation_post.objects.filter(user=request.user).filter(post=post).first()
			if query_relation is None:
				relation_value = 0
			else:
				relation_value = query_relation.reputation
		else:
			relation_value = None

		return relation_value

	def get(self, request, pk):

		post = get_object_or_404(ForumPost, id=pk)
		#title = f"Details of {server.name}"
		comments = CommentToPost.objects.all().filter(post_id=pk)
		form = CommentToPostForm

		# reputation thing, needs, if user is not authenticated, just not add this stuff overhere
		# query_relation = Reputation_post.objects.filter(user=request.user).filter(post=post).first()
		# if query_relation is None:
		# 	relation_value = 0
		# else:
		# 	relation_value = query_relation.reputation

		ctx = {
		'post':post,
		'form':form,
		'comments':comments,
		'relation_value': self.getqueryrelation(request, post),
		}

		return render(request, 'forum/forum_detail_post.html', ctx)
	def post(self, request, pk):
		
		# query_relation = Reputation_post.objects.filter(user=request.user).filter(post=post).first()
		# if query_relation is None:
		# 	relation_value = 0
		# else:
		# 	relation_value = query_relation.reputation--------------------=-=-=-------------------------------------=-=--------------------------

		if request.user.is_authenticated:
			form = CommentToPostForm(request.POST)
			if form.is_valid():
				obj = form.save(commit=False)
				obj.user = request.user
				obj.post = get_object_or_404(ForumPost, pk=pk)
				obj.save()
				print('saving!')
				return redirect('forum:forum-detail-page', pk)
			else:
				print('redirecting...')
				return render(request, 'forum/forum_detail_post.html', ctx)
		else:
			print("I'm buggy")
			ctx = {
			'post':post,
			'form':form,
			'comments':comments,
			'relation_value': self.getqueryrelation(request),
			}
			return render(request, 'forum/forum_detail_post.html', ctx)

	# def ajax_post_preputation(self, request, pk):


	# 	print(request.POST.data.user_action)

	# 	data = {
	# 	"something": request.POST.data.user_action 
	# 	}

	# 	return JsonResponse(data)

class DetailForumPostPageAjax(View):
	def post(self, request, pk):
		print(request.POST["user_action"])

		# here I need to check if user is already has opinion with post_reputation

		# get the user Entry.objects.get(pk=1)
		cur_user = User.objects.get(pk=request.POST["user_id"])

		# print(cur_user)
		post = ForumPost.objects.get(pk=request.POST["post_id"])
		# print(post)
		user_action = request.POST["user_action"]
		# print(user_action)

		# after when I got everything, I need to check if the user_profile has relation with ForumPostObject, called opinion_posts

		# if post in user.opinion_posts:
		# 	print("yes")
		# else:
		# 	print("no")

		if user_action == 'dislike':
			reputation_temp = 1
		else:
			reputation_temp = -1

		# юзер может не иметь никакого отношения к посту, тогда мы дожны создать это отношение + к тому определить, лайкнул он это пост или дизлайкнул, на основе этого
		# записать популярность
		# однако если отношение уже есть мы должны определить что юзер сделал, если он кликнул на противоположную кнопку, то мы меняем их местами
		# в соответсвие с этим выписываем отношения, если юзер кликнул на одну и туже кнопку, то мы меняем её и выписываем 0 отношение к посту, при этом каждый раз,
		# мы обновляем репутацию поста и тоже выслылаем её в response
		# querytodbtofindopinionbasedonuseridandpostid
		
		query_relation = Reputation_post.objects.filter(user=cur_user).filter(post=post).first()

		counter = 0


		if query_relation == None:
			if user_action == 'like':
				reputation_temp = 1
			elif user_action == 'dislike':
				reputation_temp = -1
			else:
				reputation_temp = 0
			print(reputation_temp)
			new_relation = Reputation_post(user=cur_user, post=post, reputation=reputation_temp)
			post.people_voted += 1
			
			post.post_reputation += new_relation.reputation
			post.save()
			new_relation.save()
			query_relation = new_relation
		# some logical erros overhere, many logical errors
		else:
			# so if reputation is greater then 0 we will check if
			if query_relation.reputation > 0:
				# it is like pressed, if so, undo the reputation and lover the people, that have been before
				if user_action == 'like':
					print("I'm right there")
					query_relation.reputation += -1
					counter = -1
					post.people_voted += -1
				# if it is dislike, we dont undo the people, but we changing the reputation
				elif user_action == 'dislike':
					query_relation.reputation += -2
					counter = -2
					print(query_relation.reputation)
				else:
				# else we do nothing
					pass
			# else if the reputation is negative (means the dislike have been pressed before)
			elif query_relation.reputation < 0:
				# we will check, if it is a like, if so we won't change the count of people, inseted change reputation
				if user_action == 'like':
					query_relation.reputation += 2
					counter += 2
				# if dislike have been pressed the second time, we will undo dislike and lower the people
				elif user_action == 'dislike':
					query_relation.reputation += 1
					post.people_voted += -1
					counter +=1
				# else we do nothing
				else:
					pass
			# if the relation exist and it is 0 and something have been pressed we will change reputation and do nothing with people, because they are counted up
			#
			else:
				print("I'm here")
				if user_action == 'like':
					query_relation.reputation = 1
					counter += 1
					post.people_voted += 1
				elif user_action == 'dislike':
					query_relation.reputation = -1
					post.people_voted += 1
					counter -= 1
				else:
					pass			
			post.post_reputation += counter
			post.save()
			query_relation.save()
		# post.post_reputation += query_relation.reputation
		

		# сформировать объект json, который отправляю обратно

		# I need to send something to dermine, which button should I show

		data = {
		"people_voted": post.people_voted,
		"reputation" : post.post_reputation,
		# send the value of query_relation.reputation
		"current_relation_reputation": query_relation.reputation
		}
		return JsonResponse(data)




# class DetailForumPageAjax(View):
# 	def post(self, request):
# 		pass



# new advanced search
class fullSearch(View):
	# generate page with get method
	def get(self, request):
		# myFilter = AdvancedForumFilter()
		# ctx = {
		# 'myFilter':myFilter,
		# }




		return render(request, 'forum/fullsearch.html')

	def post(self, request):

		# getting everything from POST dictionary
		iD = request.POST['iD']
		name = request.POST['name']
		author = request.POST['author']
		topic = request.POST['topic']
		tags = request.POST['tags']


		# logic for parsing tags by comma

		tags_individual = tags.split(',')

		tags_url = ''
		for i in range(len(tags_individual)):
			tags_url += f'&tags={tags_individual[i]}'


		rating = request.POST['rating']
		lessrating = request.POST['lessrating']
		greatrating = request.POST['greatrating']


		contains = request.POST['contains']
		date_after = request.POST['date_after']
		date_before = request.POST['date_before']

		# construct url
		url = f'/forum/?id={iD}&name={name}&user__username={author}&topic={topic}{tags_url}&greatrating={greatrating}&rating={rating}&lessrating={lessrating}&text={contains}&start_date={date_after}&end_date={date_before}'
		# redirect
		return redirect(url)

		# choices date_created, id, name, post_comment, tagged_items, tags, text, topic, user, user_id

		# queryset =

		# url = ?ForumPost__name=&

		# get what info have been sended
		# post_name = request.POST['']

		# access database model and filter eveything what we need
		# generate url for filter in forum filter view
		# forum/
		# redirect to that url
		pass





