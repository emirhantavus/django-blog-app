from rest_framework import viewsets
from ..models import User
from ..serializers import userSerializer

class userSignIn(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = userSerializer