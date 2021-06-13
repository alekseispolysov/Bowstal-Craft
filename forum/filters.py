import django_filters
from django_filters import DateFilter, CharFilter, NumberFilter
from taggit.managers import TaggableManager
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper
from django.forms.widgets import TextInput


from . models import *

class ForumFilter(django_filters.FilterSet):

	#Date_from = DateFilter(field_name="date_created", lookup_expr='gte')
	#Date_before = DateFilter(field_name="date_created", lookup_expr='lte')
	#text = CharFilter(field_name='text', lookup_expr='icontains')
	id = NumberFilter(label="ID", field_name='id', lookup_expr='exact')
	name = CharFilter(label="Name", field_name='name', lookup_expr='icontains', widget=TextInput(attrs={'placeholder':'Name'}))
	user_username = CharFilter(label="Author", field_name='user__username',lookup_expr='icontains', widget=TextInput(attrs={'placeholder':'Author'}))
	
	topic = CharFilter(label="Topic", field_name='topic', lookup_expr='icontains', widget=TextInput(attrs={'placeholder':'Topic'}))
	# icontains like where query
	tags = CharFilter(label="Tags", field_name='tags', lookup_expr='slug__icontains', widget=TextInput(attrs={'placeholder':'Tags'}))
	text = CharFilter(label="Text Contains", field_name='text', lookup_expr='icontains', widget=TextInput(attrs={'placeholder':'Text contains'}))

	start_date = DateFilter(field_name="date_created", lookup_expr='gte')
	end_date = DateFilter(field_name="date_created", lookup_expr='lte')

	# class Meta:
	# 	model = ForumPost
	# 	# exclude user filed, instead write it before you are filtering
	# 	fields = {
	# 	'name': ['icontains'],
	# 	}
		
# class AdvancedForumFilter(django_filters.FilterSet):
# 	name = CharFilter(label="Name", field_name='ForumPost__name', lookup_expr='icontains', widget=TextInput(attrs={'placeholder':'Name'}))
# 	user_username = CharFilter(label="Author", field_name='user__username',lookup_expr='icontains', widget=TextInput(attrs={'placeholder':'Author'}))
		



class ForumAdvancedFilter(django_filters.FilterSet):
	user_username = CharFilter(label="Author", field_name='user__username',lookup_expr='icontains', widget=TextInput(attrs={'placeholder':'Author'}))
	class Meta:
		model = ForumPost
		fields = '__all__'
		filter_overrides = {
            TaggableManager: {'filter_class': CharFilter},
        }