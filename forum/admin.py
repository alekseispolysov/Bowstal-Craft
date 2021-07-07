from django.contrib import admin

from . models import *

admin.site.register(ForumPost)

admin.site.register(CommentToPost)

admin.site.register(Reputation_post)


# Register your models here.
