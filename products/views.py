from django.http import HttpResponse
from django.shortcuts import render
from products.models import Product, Offer


def index(request):
    products_to_display = Product.objects.all()
    return render(request, 'index.html',
                  {'products': products_to_display})


def new(request):
    return HttpResponse('hello new world')