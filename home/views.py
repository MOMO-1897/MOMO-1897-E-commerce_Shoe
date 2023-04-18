from django.shortcuts import render, redirect
from django.views import View
from .models import *


# Create your views here.
class Base(View):
    views = {}


class Index(Base):

    def get(self, request):
        self.views['categories'] = Category.objects.all()
        self.views['sliders'] = Slider.objects.all()
        self.views['Product'] = Product.objects.all()
        self.views['info'] = Info.objects.all()
        return render(request, 'index.html', self.views)


class About(Base):

    def get(self, request):
        self.views['categories'] = Category.objects.all()
        self.views['sliders'] = Slider.objects.all()
        self.views['Product'] = Product.objects.all()
        self.views['info'] = Info.objects.all()
        self.views['brand'] = Brands.objects.all
        return render(request, 'about.html', self.views)


class Shop(Base):

    def get(self, request):
        self.views['categories'] = Category.objects.all()
        self.views['sliders'] = Slider.objects.all()
        self.views['Product'] = Product.objects.all()
        self.views['info'] = Info.objects.all()
        self.views['brand'] = Brands.objects.all
        self.views['subcategory'] = SubCategory.objects.all
        return render(request, 'shop.html', self.views)


class Contact(Base):

    def get(self, request):
        self.views['categories'] = Category.objects.all()
        self.views['sliders'] = Slider.objects.all()
        self.views['Product'] = Product.objects.all()
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


class ShopSingle(Base):

    def get(self, request):
        self.views['categories'] = Category.objects.all()
        self.views['sliders'] = Slider.objects.all()
        self.views['Product'] = Product.objects.all()
        self.views['info'] = Info.objects.all()
        self.views['brand'] = Brands.objects.all
        return render(request, 'shop-single.html', self.views)


class SearchView(Base):
    def get(self, request):
        self.views['categories'] = Category.objects.all()
        self.views['sliders'] = Slider.objects.all()
        self.views['Product'] = Product.objects.all()
        self.views['info'] = Info.objects.all()
        self.views['brand'] = Brands.objects.all
        query = request.GET.get('query')
        if query != "":
            self.views['search_product'] = Product.objects.filter(name__icontains=query)
        else:
            return redirect('/')
        return render(request, 'search.html', self.views)


class CategoryView(Base):
    def get(self, request, slug):
        self.views['categories'] = Category.objects.all()
        self.views['sliders'] = Slider.objects.all()
        self.views['Product'] = Product.objects.all()
        self.views['info'] = Info.objects.all()
        self.views['brand'] = Brands.objects.all

        ids = Category.objects.get(slug=slug).id
        self.views['product_category'] = Product.objects.filter(category_id=ids)
        return render(request, 'Categoryview.html', self.views)


class ProductView(Base):
    def get(self, request, slug):
        self.views['categories'] = Category.objects.all()
        self.views['sliders'] = Slider.objects.all()
        self.views['Product'] = Product.objects.all()
        self.views['info'] = Info.objects.all()
        self.views['brand'] = Brands.objects.all

        self.views['product_specific'] = Product.objects.filter(slug=slug)
        return render(request, 'product.html', self.views)
