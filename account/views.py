from django.shortcuts import redirect, render
from .forms import *
from django.contrib.auth import login, authenticate
from django.views import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

# Create your views here.


def signup(request):
    if request.method == 'POST':
        context={}
        form = signupForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=password)
            login(request, user)
            context['status']="account has been successfully created"
    else:
        form = signupForm()
    return render(request, 'account/signup.html', {'form': form})




class login_view(View):
    def get(self,request,*args,**kwargs):
        return render(request,"account/login.html",{})

    def post(self,request,*args,**kwargs):
        context={}
        email = request.POST.get("email")	
        password = request.POST.get("password")
        user=authenticate(email=email,password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            context['status']="email and password is not exists" 	
        return render(request,"account/login.html",context)	


class index(View):
    @method_decorator(login_required)
    def get(self,request,*args,**kwargs):
        return render(request,"account/index.html",{})