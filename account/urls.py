from django.urls import path
from django.urls.conf import include
from .views import *
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path("signup",signup,name="signup"),
    path("login",login_view.as_view(),name="login"),
    path("",index.as_view(),name="index")
   
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
