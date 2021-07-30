from django.test import TestCase, Client
from django.urls import reverse
from forum.models import ForumPost
from django.contrib.auth.models import User
import json

class TestViews(TestCase):
	def setUp(self):
		self.client = Client()
		# getting user from user database
		self.user = User.objects.create_user(username='testuser', password='12345')
		# urls
		self.ForumPostCreateUrl = reverse('forum:forum-create-post')
		self.ForumPostDetailUrl = reverse('forum:forum-detail-page', args=['1'])
		self.ForumPostUpdateUrl = reverse('forum:forum-update-post', args=['1'])
		self.ForumPostDeleteUrl = reverse('forum:forum-delete-post', args=['1'])
		# instances
		self.ForumPost1 = ForumPost.objects.create(
			user = self.user,
			name = 'The best post for test posts on forum',
			topic = 'Important',
			tags = ['test'],
			content = 'Block content',
			)
	# just post it and run away, I have a form for delete, with just one button submit. If I click button. It sumbits, so from, without data and just submit
	# lookup why you are getting not, what you want from deleting!

	# def test_ForumPost_DELETE_post(self):
		
		
	# 	response = self.client.delete(self.ForumPostDeleteUrl)

	# 	self.assertEquals(response.status_code, 302)
	# 	self.assertEquals(self.ForumPost1, None)

