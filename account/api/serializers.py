from rest_framework.fields import Field
from ..models import Account
from rest_framework.serializers import ModelSerializer, Serializer, CharField, ImageField, SerializerMethodField


class accountSerializer(ModelSerializer):
    class Meta:
        model = Account
        fields = ['email','full_name']