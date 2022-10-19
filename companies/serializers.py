from rest_framework import serializers
from .models import Company
from accounts.serializers import UserSerializer
from advocates.serializers import DeveloperSerializer



class CompanyListSerializer(serializers.ModelSerializer):
    advocates = DeveloperSerializer(many=True)
    owner = UserSerializer(many=False)
    class Meta:
        model = Company
        fields = ('id','owner','name','logo','email','advocates')


