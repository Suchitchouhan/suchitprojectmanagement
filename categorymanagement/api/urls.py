from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
   path("getcategorylist",getcategorylist.as_view(),name="getcategorylist")

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
