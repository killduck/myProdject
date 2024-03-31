

from django.shortcuts import render
from .models import Products


def index(request):

    products = Products.objects.all()

    print(f'10 {products}')

    return render(request, 'index.html', {'products': products})

