from ..models import category
from rest_framework.serializers import ModelSerializer, Serializer, CharField, ImageField, SerializerMethodField


class categorySerializer(ModelSerializer):
    class Meta:
        model = category
        fields = ['name','description']