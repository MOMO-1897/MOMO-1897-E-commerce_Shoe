from django.shortcuts import render
from django.views import View


# Create your views here.
class Base(View):
    views = {}


class Index(Base):

    def get(self, request):
        return render(request, 'index.html')


class About(Base):

    def get(self, request):
        return render(request, 'about.html')

class Shop(Base):

    def get(self, request):
        return render(request, 'shop.html')

class Contact(Base):

    def get(self, request):
        return render(request, 'contact.html')

