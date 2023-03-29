from django.shortcuts import render
from django.views import View


# Create your views here.
class Base(View):
    views = {}


class HomeView(Base):

    def get(self, request):
        return render(request, 'index.html')
