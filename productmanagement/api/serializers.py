from ..models import product
from rest_framework.serializers import ModelSerializer, Serializer, CharField, ImageField, SerializerMethodField


class productSerializer(ModelSerializer):
    category=SerializerMethodField()
    def get_category(self, instance):
        return instance.category.name
    class Meta:
        model = product
        fields = ['id','name','category','price','image']