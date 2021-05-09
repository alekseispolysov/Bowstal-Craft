from django.contrib import admin

from . models import *

admin.site.register(ForumPost)

admin.site.register(CommentToPost)

# Register your models here.
