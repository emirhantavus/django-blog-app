from rest_framework import serializers
from ..models import Comment

class commentSerializer(serializers.ModelSerializer):
      author = serializers.StringRelatedField()
      commentDate = serializers.DateTimeField(format='%Y-%m-%d %H:%M')
      class Meta:
            model = Comment
            fields = ('author','content','commentDate')