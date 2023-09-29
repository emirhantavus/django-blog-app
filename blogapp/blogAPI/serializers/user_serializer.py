from rest_framework import serializers
from ..models import User

class userSerializer(serializers.ModelSerializer):
      date_joined = serializers.DateField(format='%d/%m/%Y',input_formats=['%d/%m/%Y'])
      class Meta:
            model = User
            fields = ('id','username','is_active','is_staff','date_joined')