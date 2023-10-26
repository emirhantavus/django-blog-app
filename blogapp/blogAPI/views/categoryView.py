from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models import Category
from ..serializers import categorySerializer

class categoryOP(APIView):
      def get(self,request):
            try:
                  query = Category.objects.all()
                  serializer = categorySerializer(query,many=True)
                  return Response(serializer.data,status=status.HTTP_200_OK)
            except:
                  return Response({'message':'error'},status=status.HTTP_404_NOT_FOUND)
      
      def post(self,request):
            serializer = categorySerializer(data=request.data)
            if serializer.is_valid():
                  serializer.save()
                  return Response({'message':'creat   ed'},status=status.HTTP_201_CREATED)
            else:
                  return Response({'message':'error'},status=status.HTTP_400_BAD_REQUEST)