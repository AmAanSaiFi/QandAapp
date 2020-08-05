from django.contrib import admin
from . models import Title,Question,Post
# Register your models here.

admin.site.register(Title)
admin.site.register(Question)
admin.site.register(Post)
