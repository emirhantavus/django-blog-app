from django.db import models
from .post import Post
from .user import User

class Comment(models.Model):
      post = models.ForeignKey(Post, on_delete=models.CASCADE)
      author = models.ForeignKey(User,on_delete=models.CASCADE)
      content = models.TextField(max_length=2048)
      commentDate = models.DateTimeField()
      
      def __str__(self) -> str:
            return f'a comment in {self.post} from {self.author}'