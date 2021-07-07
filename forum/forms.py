from django import forms
from django.forms import ModelForm
from crispy_forms.helper import FormHelper
#from django.forms.models import modelformset_factory
from . models import *

class ForumPostForm(ModelForm):
	
	class Meta:
		model = ForumPost
		# fields= '__all__'
		fields = ['name', 'topic', 'tags', 'content']
		# exclude = ('user',',date_sent',)


# post comment form
class CommentToPostForm(ModelForm):
	text = forms.CharField(widget=forms.Textarea, label='')
	class Meta:
		model = CommentToPost
		fields = ['text']


# class ForumPostAdvancedSearch(ModelForm):

# 	class Meta:
# 		model = ForumPost
# 		fields = '__all__'
# 		exclude = ('')
