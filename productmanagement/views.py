from django.http import request
from django.shortcuts import get_object_or_404, render
from django.shortcuts import redirect, render
from .forms import *
from django.contrib.auth import login, authenticate
from django.views import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

# Create your views here.
class views_product(View):
    @method_decorator(login_required)
    def get(self,request):
        context={}
        p=product.objects.all().order_by("-id")
        context['product']=p
        context['form1']=productForm()
        return render(request,'account/views_product.html',context)

    @method_decorator(login_required)
    def post(self,request):
        context={}
        form= productForm(request.POST)
        if form.is_valid():
            form.save()
            context['status']="product has been successfully added"
        else:
            context['status']="Something worng"
        p=product.objects.all().order_by("-id")
        context['product']=p
        context['form1']=productForm()
        return render(request,'account/views_product.html',context)      


class add_product(View):
    @method_decorator(login_required)
    def get(self,request):
        context={}
        cat=category.objects.all()
        context['categroy']=cat
        return render(request,'account/add_product.html',context)

          


def delete(request,pk):
    if product.objects.filter(pk=pk).exists():
        p=product.objects.get(pk=pk)
        p.delete()
        return redirect("/product/views_product")
        

def update(request,pk):
    context={}
    if request.method == "POST":
        obj = get_object_or_404(product, id = pk)
        form= productForm(request.POST)
        if form.is_valid():
            form.save()
            context['status']="product has been successfully update"
        else:
            context['status']="Something worng"
        return render(request,'account/views_product.html',context)     
    else:        
        return render(request,'account/views_product.html',context) 
                
