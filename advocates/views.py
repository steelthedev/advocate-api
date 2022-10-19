from .serializers import DeveloperSerializer
from .models import Developer
from rest_framework.views import APIView
from rest_framework.response import Response

class DeveloperListView(APIView):

    def get_objects(self):
        return Developer.objects.all()


    def get(self,request):
        company = self.get_objects()
        serializer = DeveloperSerializer(company, many=True)
        return Response(serializer.data)