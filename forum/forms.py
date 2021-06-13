from django.forms import ModelForm
from crispy_forms.helper import FormHelper
#from django.forms.models import modelformset_factory
from . models import *

class ForumPostForm(ModelForm):
	
	class Meta:
		model = ForumPost
		fields= '__all__'
		exclude = ('user','date_sent',)


# class ForumPostAdvancedSearch(ModelForm):

# 	class Meta:
# 		model = ForumPost
# 		fields = '__all__'
# 		exclude = ('')
