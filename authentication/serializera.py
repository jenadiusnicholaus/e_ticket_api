from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer
from .models import CustomUser


class UserSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['url', 'username', 'email', 'is_staff']
