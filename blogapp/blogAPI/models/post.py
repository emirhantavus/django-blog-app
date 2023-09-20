from django.db import models

class Post(models.Model):
      author = models.ForeignKey() # User, on_delete CASCADE...
      title = models.CharField(max_length=256)
      content = models.TextField()
      postDate = models.DateTimeField()
      
      def __str__(self) -> str:
            return self.title