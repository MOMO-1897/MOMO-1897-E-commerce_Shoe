from .views import *
from django.urls import path

urlpatterns = [
   path('', Index.as_view(), name='index'),
   path('index.html', Index.as_view(), name='index'),
   path('about.html', About.as_view(), name='about'),
   path('shop.html', Shop.as_view(), name='shop'),
   path('contact.html', Contact.as_view(), name='shop')
]
