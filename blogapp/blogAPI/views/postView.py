from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models import Post , Comment
from ..serializers import postSerializer , commentSerializer

class postList(APIView):
      def get(self,request):
            page = int(request.GET.get('page',1))
            per_page = 10
            start = (page-1) * per_page
            end = start + per_page
            posts = Post.objects.all()[start:end]
            serializer = postSerializer(posts,many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)
      
      def post(self,request):
            serializer = postSerializer(data=request.data)
            if serializer.is_valid():
                  serializer.save()
                  return Response({'Message':'Post created'},status=status.HTTP_201_CREATED)

class singlePostList(APIView):
      def get(self,request,pk):
            try:
                  post = Post.objects.get(pk=pk)
                  comments = Comment.objects.filter(post = post)
                  post_data = {
                  "title": post.title,
                  "content": post.content,
                  "category": post.category.name,
                  "author": post.author.username,
                  "postDate": post.postDate,
                  "comment": commentSerializer(comments, many=True).data
                  }
                  return Response(post_data)
            except Post.DoesNotExist:
                  return Response({'message': 'Post not found'}, status=status.HTTP_404_NOT_FOUND)