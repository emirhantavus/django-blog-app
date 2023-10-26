from django.db import models
from .userModel import User
from .categoryModel import Category


class Post(models.Model):
      author = models.ForeignKey(User,on_delete=models.CASCADE)
      title = models.CharField(max_length=256)
      content = models.TextField()
      postDate = models.DateTimeField()
      category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True,blank=True)
      
      def __str__(self):
            return f'author: {self.author} title: {self.title}'