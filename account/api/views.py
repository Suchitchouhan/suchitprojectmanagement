from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from .serializers import *
from ..models import Account



class getaccountlist(ListAPIView):
    queryset = Account.objects.all()

    def get(self, request):
        qs = self.get_queryset()
        data = accountSerializer(qs, many=True).data
        return Response({'data':data},status=HTTP_200_OK)