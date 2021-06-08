from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
   path("allproduct",allproduct.as_view(),name="allproduct"),
   path("allproductbycategory/<int:pk>",allproductbycategory.as_view()),
   path("productdetail/<int:pk>",productdetail.as_view())


]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
