from django.contrib import admin

from . models import *

# Register your models here.

admin.site.register(Post)
admin.site.register(ContactEmail)
admin.site.register(SecurityEmailMessage)
admin.site.register(CommentToPost)