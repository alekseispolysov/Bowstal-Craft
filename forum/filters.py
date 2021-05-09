import django_filters
from django_filters import DateFilter, CharFilter
from taggit.managers import TaggableManager
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper
from django.forms.widgets import TextInput


from . models import *

class ForumFilter(django_filters.FilterSet):

	#Date_from = DateFilter(field_name="date_created", lookup_expr='gte')
	#Date_before = DateFilter(field_name="date_created", lookup_expr='lte')
	#text = CharFilter(field_name='text', lookup_expr='icontains')
	name = CharFilter(label="Name", field_name='ForumPost__name', lookup_expr='icontains', widget=TextInput(attrs={'placeholder':'Name'}))
	user_username = CharFilter(label="Author", field_name='user__username',lookup_expr='icontains', widget=TextInput(attrs={'placeholder':'Author'}))
	# class Meta:
	# 	model = ForumPost
	# 	# exclude user filed, instead write it before you are filtering
	# 	fields = {
	# 	'name': ['icontains'],
	# 	}
		
