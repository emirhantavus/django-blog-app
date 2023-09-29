from rest_framework import serializers
from ..models import Comment

class commentSerializer(serializers.ModelSerializer):
      commentDate = serializers.DateField(format='%d/%m/%Y',input_formats=['%d/%m/%Y'])
      class Meta:
            model = Comment
            fields = ('author','post','commentDate')