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
        self.views['categories'] = Category.objects.all()
        self.views['sliders'] = Slider.objects.all()
        self.views['subcategory'] = SubCategory.objects.all()
        self.views['info'] = Info.objects.all()
        self.views['brand'] = Brands.objects.all
        return render(request, 'about.html', self.views)


class Shop(Base):

    def get(self, request):
        return render(request, 'shop.html')


class Contact(Base):

    def get(self, request):
        self.views['categories'] = Category.objects.all()
        self.views['sliders'] = Slider.objects.all()
        self.views['subcategory'] = SubCategory.objects.all()
        self.views['info'] = Info.objects.all()
        self.views['brand'] = Brands.objects.all
        if request.method == "POST":
            name = request.POST['name']
            email = request.POST['email']
            subject = request.POST['subject']
            message = request.POST['message']
            contact = ContactUs(name=name, email=email, Subject=subject, Message=message)
            contact.save()
            return render(request, 'contact.html', self.views)
        else:
            return render(request, 'contact.html', self.views)
