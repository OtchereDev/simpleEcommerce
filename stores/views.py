from django.shortcuts import render
from .models import *

def store(request):
    product=Product.objects.all()
    context={'products':product}
    return render(request,'store/store.html',context=context)

def checkout(request):
    context={}
    return render(request,'store/checkout.html',context=context)

def cart(request):
    context={}
    return render(request,'store/cart.html',context=context)