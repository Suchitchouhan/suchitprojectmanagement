from django.urls import path
from django.urls.conf import include
from .views import *
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path("view_category",view_category.as_view(),name="index"),
    path("delete_Category/<int:pk>",delete_Category.as_view(),name="delete_Category"),
   
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
