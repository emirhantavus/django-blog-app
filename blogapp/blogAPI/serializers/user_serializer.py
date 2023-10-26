# users/serializers.py
from rest_framework import serializers
from ..models import User

class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email','password','last_login')
        extra_kwargs = {'password': {'write_only': True}}
    
    def create(self, validated_data):
            user = User.objects.create_user(
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email'],
            password=validated_data['password']
        )
            return user
