from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Product
from datetime import datetime


def home(request):
    products = Product.objects
    return render(request, 'products/home.html', {'products': products})


@login_required()
def create(request):
    if request.method == "POST":
        data = request.POST
        if data['title'] and data['body'] and data['url'] and request.FILES['icon'] and request.FILES['image']:
            product = Product()
            product.title = data['title']
            product.body = data['body']
            if data['url'].startswith('http://') or data['url'].startswith('https://'):
                product.url = data['url']
            else:
                product.url = 'http://' + data['url']
            product.icon = request.FILES['icon']
            product.image = request.FILES['image']
            product.pub_date = datetime.now()
            product.hunter = request.user
            product.save()
            return redirect('/products/' + str(product.id))
        else:
            return render(request, 'products/create.html', {'error': 'All fields are mandatory'})
    else:
        return render(request, 'products/create.html')


def detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'products/detail.html', {'product': product})


@login_required
def inc_count(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    product.votes_count += 1
    product.save()
    return redirect('/products/' + str(product.id))
