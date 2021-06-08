from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from .serializers import *
from ..models import category



class getcategorylist(ListAPIView):
    queryset = category.objects.all()

    def get(self, request):
        qs = self.get_queryset()
        data = categorySerializer(qs, many=True).data
        return Response({'data':data},status=HTTP_200_OK)