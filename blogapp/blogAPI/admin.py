from django.contrib import admin
from .models import Post
from .models import Comment
from .models import User
# Register your models here.
admin.site.register(User)
admin.site.register(Post)
admin.site.register(Comment)