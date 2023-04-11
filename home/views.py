from django.shortcuts import render
from django.views import View
from .models import *


# Create your views here.
class Base(View):
    views = {}


class Index(Base):

    def get(self, request):
        self.views['categories'] = Category.objects.all()
        self.views['sliders'] = Slider.objects.all()
        self.views['subcategory'] = SubCategory.objects.all()
        self.views['info'] = Info.objects.all()
        return render(request, 'index.html', self.views)


class About(Base):

    def get(self, request):
        return render(request, 'about.html')


class Shop(Base):

    def get(self, request):
        return render(request, 'shop.html')


class Contact(Base):

    def get(self, request):
        return render(request, 'contact.html')

