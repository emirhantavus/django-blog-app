from django.db import models
from .post import Post

class Comment(models.Model):
      post = models.ForeignKey(Post, on_delete=models.CASCADE)
      author = models.ForeignKey()   # User, on_delete=models.CASCADE
      content = models.TextField(max_length=2048)
      commentDate = models.DateTimeField()
      
      def __str__(self) -> str:
            return self.content