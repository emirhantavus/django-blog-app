from rest_framework.views import APIView
from rest_framework.response import Response
from ..models import Category
from ..serializers import categorySerializer

class categoryOP(APIView):
      def get(self,request):
            query = Category.objects.all()
            serializer = categorySerializer(query,many=True)
            return Response(serializer.data)