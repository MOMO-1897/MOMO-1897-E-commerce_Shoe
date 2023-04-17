from django.template.defaulttags import url

from . import views
from .views import *
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

app_name = 'home'

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('index.html', Index.as_view(), name='index'),
    path('about.html', About.as_view(), name='about'),
    path('shop.html', Shop.as_view(), name='shop'),
    path(r'contact', views.Contact.as_view(), name='contact'),
    path('contact.html', Contact.as_view(), name='contact'),
    path('shop-single.html', ShopSingle.as_view(), name='shopsingle'),
    path('search', SearchView.as_view(), name='search'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
