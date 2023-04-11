from .views import *
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
   path('', Index.as_view(), name='index'),
   path('index.html', Index.as_view(), name='index'),
   path('about.html', About.as_view(), name='about'),
   path('shop.html', Shop.as_view(), name='shop'),
   path('contact.html', Contact.as_view(), name='shop')
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
