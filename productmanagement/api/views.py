from categorymanagement.models import category
from django.db import models
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from .serializers import *
from ..models import product


class allproduct(ListAPIView):
    def get(self,request):
        context={}
        p=product.objects.all()
        context['product']=productSerializer(p,many=True).data
        return Response(context)


class allproductbycategory(ListAPIView):
    def get(self,request,*args,**kwargs):
        context={}
        pk=self.kwargs['pk']
        c=category.objects.get(pk=pk)
        p=product.objects.filter(category=c)
        context['product']=productSerializer(p,many=True).data
        return Response(context)        



class productdetail(APIView):
    def get(self,request,*args,**kwargs):
        context={}
        pk=self.kwargs['pk']
        p=product.objects.get(pk=pk)
        context['product']=productSerializer(p,many=False).data
        return Response(context)                