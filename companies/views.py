
from .serializers import CompanyListSerializer
from .models import Company
from rest_framework.views import APIView
from rest_framework.response import Response

class CompanyView(APIView):

    def get_objects(self):
        return Company.objects.all()


    def get(self,request):
        company = self.get_objects()
        serializer = CompanyListSerializer(company, many=True)
        return Response(serializer.data)