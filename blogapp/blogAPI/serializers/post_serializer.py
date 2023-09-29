from rest_framework import serializers
from ..models import Post

class postSerializer(serializers.ModelSerializer):
      postDate = serializers.DateField(format='%d/%m/%Y',input_formats=['%d/%m/%Y'])
      class Meta:
            model = Post
            fields = ('author','title','postDate')