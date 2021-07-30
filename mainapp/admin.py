from django.contrib import admin

from django_admin_filter.filters import CustomFilter # importing admin filters module

from . models import *

# Register your models here.

# class MyAdmin(admin.ModelAdmin):
#    list_filter = [CustomFilter]




admin.site.register(Post)
admin.site.register(ContactEmail)
admin.site.register(SecurityEmailMessage)
admin.site.register(CommentToPost)