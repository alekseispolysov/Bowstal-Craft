from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.views import generic
from django.views import View


from . models import *
from . forms import *
from . filters import *

# detail view of the post
class PostDetailPage(View):
	#login_url = '/user/login/'
	def get(self, request, pk):

		post = get_object_or_404(Post, id=pk)
		#title = f"Details of {server.name}"
		comments = CommentToPost.objects.all().filter(post_id=pk)
		form = CommentToPostForm
		ctx = {
		'post':post,
		'form':form,
		'comments':comments,
		}
		return render(request, 'mainapp/post_detail.html', ctx)
	def post(self, request, pk):
		if request.user.is_authenticated:
			form = CommentToPostForm(request.POST)
			if form.is_valid():
				obj = form.save(commit=False)
				obj.user = request.user
				obj.post = get_object_or_404(Post, pk=pk)
				obj.save()
				print('saving!')
				return redirect('mainapp:post-detail', pk)
			else:
				print('redirecting...')
				return render(request, 'mainapp/post_detail.html', ctx)
		else:
			print("I'm buggy")
			ctx = {
			'post':post,
			'form':form,
			'comments':comments,
			}
			return render(request, 'mainapp/post_detail.html', ctx)
# home page


class HomePage(View):
	def get(self, request):
		return render(request, 'mainapp/home_page.html')

# newspage
class NewsPage(generic.ListView):
	template_name = 'mainapp/home.html'
	paginate_by = 5
	model = Post

	def get_queryset(self):
		self.news_count = Post.objects.all().count()
		queryset = super(NewsPage, self).get_queryset()
		# reverse queryset
		return queryset[::-1]

	def get_context_data(self, **kwargs):
		ctx = super().get_context_data(**kwargs)
		ctx['news_count'] = self.news_count
		# ctx['importantObjects'] = ForumPost.objects.all().filter(topic__icontains="Important")
		return ctx


class NewsAllPage(generic.ListView):
	template_name = 'mainapp/news_all.html'
	model = Post
	def get_queryset(self):
		news = Post.objects.all()
		# filter all usernames
		queryset = super(NewsAllPage, self).get_queryset()

		

		#qs = sorted(queryset_chain)

		self.myFilter = newsFilter(self.request.GET, queryset=news)
		# здесь прибавить important посты (если топика импортант)
		
		# print(self.important_post)
		queryset = self.myFilter.qs 
		return queryset

	def get_context_data(self, **kwargs):
		ctx = super().get_context_data(**kwargs)
		ctx['myFilter'] = self.myFilter
		# ctx['importantObjects'] = ForumPost.objects.all().filter(topic__icontains="Important")
		return ctx


# about page
class AboutPage(View):
	def get(self, request):
		return render(request, 'mainapp/about_page.html')

# support us page
class SupportUs(View):
	def get(self, request):
		return render(request, 'mainapp/support_us_page.html')

# download page
class DownloadPage(View):
	def get(self, request):
		return render(request, 'mainapp/download_page.html')



# footer contact form + contact form in contact form view
class ContactPage(FormView):
	def get(self, request):
		form = ContactEmailsForm()
		ctx = {
		'form':form,
		}
		return render(request, 'mainapp/contact_page.html', ctx)
	def post(self, request):
		form = ContactEmailsForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('mainapp:confirm-contact-page')
		else:
			ctx = {
			'form':form,
			}
			return render(request, 'mainapp/contact_page.html', ctx)
		# save email to the database


		# redirect the user to confirm page
		



# if the user sended their mail correct, they would be redirected to the confirmed view
class ConfirmPage(View):
	def get(self, request):
		return render(request, 'mainapp/contact_confirm_page.html')



# view of the security page
class SecurityContactPage(FormView):
	def get(self, request):
		form = SecutiryMainForm()
		ctx = {
		'form':form,
		}
		return render(request, 'mainapp/security_bug_send.html', ctx)
	def post(self, request):
		form = SecutiryMainForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('mainapp:secutiry-report-success')
		else:
			ctx = {
			'form':form,
			}
			return render(request, 'mainapp/security_bug_send.html', ctx)

class SuccessSecurityPage(View):
	def get(self, request):
		return render(request, 'mainapp/security_success.html')



	# def get(self, request):
	# 	form = SecutiryMainForm
	# 	ctx = {
	# 	'form':form,
	# 	}
	# 	return render(request, 'mainapp/contact_page.html', ctx)
	# def post(self, request):
	# 	form = ContactEmailsForm(request.POST)
	# 	if form.is_valid():
	# 		form.save()
	# 		return redirect('mainapp:confirm-contact-page')
	# 	else:
	# 		ctx = {
	# 		'form':form,
	# 		}
	# 		return render(request, 'mainapp/contact_page.html', ctx)






