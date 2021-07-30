from django.test import TestCase, Client
from django.urls import reverse
from mainapp.models import Post, ContactEmail
import json


class TestViews(TestCase):

	# exactly that name please
	def setUp(self):
		# setup test client
		self.client = Client()
		# urls
		self.ContactPageUrl = reverse('mainapp:contact-page')
		self.PostDeailPageUrl = reverse('mainapp:post-detail', args=['1'])
		# test instances of a posts
		self.project1 = Post.objects.create(
			name='Well you got me',
			text='lorem 100',
			preview_text='Check me out'
			)

	def test_ContactPage_GET(self):

		response = self.client.get(self.ContactPageUrl)

		self.assertEquals(response.status_code, 200)
		# test if certain template is used
		self.assertTemplateUsed(response, 'mainapp/contact_page.html')

	def test_ContactPage_POST_adds_new_contactMessage(self):
		# ContactEmail.objects.create(
			
		# 	)
		# :)
		#  while building a form wathing for email= and 'email':, if you using correct url and so on
		response = self.client.post(self.ContactPageUrl, data={
			'email' : 'Perematom@gmail.com',
			'subject' : 'I\'d like to drink some coffe with you',
			'text' : 'Lorem my message. I need help... Beep... Beep.. Please stand by/\\/'
			})

		self.assertEquals(response.status_code, 302) # riderect here
		mine_email_message = ContactEmail.objects.get(pk=1)
		self.assertEquals(mine_email_message.email, 'Perematom@gmail.com')

	def test_ContactPage_POST_no_data(self):
		response = self.client.post(self.ContactPageUrl)

		self.assertEquals(response.status_code, 200) # riderect here

		self.assertEquals(ContactEmail.objects.get(pk=1), None)

	def test_PostDetailPage_GET(self):

		response = self.client.get(self.PostDeailPageUrl)

		self.assertEquals(response.status_code, 200)
		# test if certain template is used
		self.assertTemplateUsed(response, 'mainapp/post_detail.html')		


