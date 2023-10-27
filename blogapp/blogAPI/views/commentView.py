# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models import Comment
from ..serializers import commentSerializer

class commentList(APIView):
    def get(self, request):
        comments = Comment.objects.all()
        serializer = commentSerializer(comments, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = commentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
