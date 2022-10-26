from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Category

def start(response):
    categories = Category.objects.all()
    products = Product.objects.all()
    return render(response, 'main/start.html', categories, products)

# Create your views here.
def end(response):
    return render(response, 'main/end.html')