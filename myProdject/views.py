

from django.shortcuts import render
from .models import Product


def index(request):

    products = Product.objects.all()

    print(f'10 {products}')

    return render(request, 'index.html', {'products': products})

