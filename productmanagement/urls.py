from django.urls import path
from django.urls.conf import include
from .views import *
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path("views_product",views_product.as_view(),name="views_product"),
    path("add_product",add_product.as_view(),name="add_product"),
    path("delete/<int:pk>",delete,name="delete"),
    path("update/<int:pk>",update,name="update"),
   
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
