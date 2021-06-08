
from django.shortcuts import redirect, render
from .forms import *
from django.contrib.auth import login, authenticate
from django.views import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

class view_category(View):
    @method_decorator(login_required)
    def get(self,request,*args,**kwargs):
        context={}
        context['category']=category.objects.all().order_by("-id")
        return render(request,"account/category.html",context)

    @method_decorator(login_required)
    def post(self, request,*args,**kwargs):
        context={}
        form=categoryForm(request.POST)
        if form.is_valid():
            form.save()
            context['status']="category is added successfully"
        else:
            context['status']="something worng"   
        context['category']=category.objects.all().order_by("-id")
        return render(request,"account/category.html",context)


class delete_Category(View):
     def get(self,request,*args,**kwargs):
        pk=self.kwargs['pk']
        c=category.objects.get(pk=pk)
        c.delete()
        return redirect("/category/view_category")