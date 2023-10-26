from rest_framework import serializers
from ..models import Post

class postSerializer(serializers.ModelSerializer):
      postDate = serializers.DateTimeField(format='%Y-%m-%d %H:%M')
      author = serializers.StringRelatedField()
      category = serializers.StringRelatedField()
      class Meta:
            model = Post
            fields = ('title','content','category','author','postDate')