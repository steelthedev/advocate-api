from rest_framework import serializers
from .models import Developer
from companies.serializers import UserSerializer



class DeveloperSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False)
    class Meta:
        model = Developer
        fields = ('id','user')


class DeveloperDetailsSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False)
    class Meta:
        model = Developer
        fields = ('id','user','company')