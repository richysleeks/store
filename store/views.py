from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):
    context = {

    }
    return render(request, 'store/home.html',context)

def product(request, id):
    context = {

    }
    return render(request, 'store/product.html',context)

def cart(request):
    context = {

    }
    return render(request, 'store/order_summary.html',context)

def checkout(request):
    context = {

    }
    return render(request, 'store/checkout.html',context)
