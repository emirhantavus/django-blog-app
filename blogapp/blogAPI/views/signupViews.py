#from rest_framework import viewsets
#from rest_framework.generics import ListAPIView , CreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models import User
from ..serializers import userSerializer

'''
class userSignIn(viewsets.ModelViewSet): #for all crud operations we use viewsets.
    queryset = User.objects.all()
    serializer_class = userSerializer
    
class getUsers(ListAPIView): for create users.
      queryset = User.objects.all()
      serializer_class = userSerializer
'''

class userModelView(APIView):
      def get(self,request):
            users = User.objects.all()
            serializer = userSerializer(users,many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)
      
      def post(self,request):
            serializer = userSerializer(data=request.data)
            if serializer.is_valid():
                  serializer.save()
                  return Response({'Message':'User created'},status=status.HTTP_201_CREATED)


class singleUserModelView(APIView):
      def get(self,request,pk):
            try:
                  user = User.objects.get(pk=pk)
                  serializer = userSerializer(user)
                  return Response(serializer.data,status=status.HTTP_200_OK)
            except:
                  return Response({"message":"User not found"},status=status.HTTP_404_NOT_FOUND)
      
      def put(self,request,pk):
            try:
                  user = User.objects.get(pk=pk)
                  serializer = userSerializer(user , data=request.data,partial=True)
                  if serializer.is_valid():
                        serializer.save()
                        return Response(serializer.data,status=status.HTTP_200_OK)
                  return Response({"message":"error"},status=status.HTTP_400_BAD_REQUEST)
            except User.DoesNotExist:
                  return Response({"message":"user not found"},status.HTTP_404_NOT_FOUND)
            
      def delete(self,request,pk):
            try:
                  user = User.objects.get(pk=pk)
                  user.delete()
                  return Response({"message":"User deleted"},status=status.HTTP_204_NO_CONTENT)
            except User.DoesNotExist:
                  return Response({"message":"User not found"},status=status.HTTP_404_NOT_FOUND)
                  