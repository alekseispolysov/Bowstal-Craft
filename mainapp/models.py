from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
	name = models.CharField(max_length=30, null=True)
	text = RichTextUploadingField(null=True, blank=True)
	preview_text = models.CharField(max_length=400, null=True, blank=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	preview_picture = models.ImageField(default="home_posts/sample_image.jpg", null=True, blank=True)

	def __str__(self):
		return self.name

class CommentToPost(models.Model):
	user = models.ForeignKey(User, related_name="user_comment_news", blank=True, null=True, on_delete=models.CASCADE)
	post = models.ForeignKey(Post, related_name="post_comment_news", blank=True, null=True, on_delete=models.CASCADE)
	text = models.TextField(null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)

	def __str__(self):
		return str(self.date_created) + ' ' + self.post.name + ' ' + self.user.username


class ContactEmail(models.Model):
	email = models.EmailField(max_length=30, null=True)
	subject = models.CharField(max_length=50, null=True)
	text = models.TextField(null=True)
	date_sent = models.DateTimeField(auto_now_add=True, null=True)

	def __str__(self):
		return self.subject + ' ' + self.email

class SecurityEmailMessage(models.Model):
	CATEGORY = (
		('Bug on website', 'Bug on website'),
		('Suggestions', 'Suggestions'),
		('Help', 'Help'),
		('Bug on server','Bug on server'),
		('Bug with plugins', 'Bug with plugins'),
		('Other', 'Other'),
	)
	email = models.EmailField(max_length=30, null=True)
	subject = models.CharField(max_length=50, null=True)
	topic = models.CharField(max_length=100, null=True, choices=CATEGORY)
	text = RichTextUploadingField(null=True)
	date_sent = models.DateTimeField(auto_now_add=True, null=True)

	def __str__(self):
		return self.subject + ' ' + self.topic + ' ' + self.email