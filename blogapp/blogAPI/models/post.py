from django.db import models
from .user import User

class Post(models.Model):
      author = models.ForeignKey(User,on_delete=models.CASCADE)
      title = models.CharField(max_length=256)
      content = models.TextField()
      postDate = models.DateTimeField()
      
      def __str__(self):
            return f'author: {self.author} title: {self.title}'