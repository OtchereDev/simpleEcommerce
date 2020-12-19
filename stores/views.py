from django.shortcuts import render
from django.http import JsonResponse
import datetime

import json

from .models import *

def store(request):
    product=Product.objects.all()
    if request.user.is_authenticated:
        customer=request.user.customer
        order,created=Order.objects.get_or_create(customer=customer,complete=False)
        items=order.orderitem_set.all()
        cartItems=order.get_cart_items
    else:
        items=[]
        order={'get_cart_total':0,
        'get_cart_items':0}
        cartItems=order.get_cart_items

    context={'products':product,'cartItems':cartItems,'shipping':False}
    return render(request,'store/store.html',context=context)

def checkout(request):
    if request.user.is_authenticated:
        customer=request.user.customer
        order,created=Order.objects.get_or_create(customer,complete=False)
        items=order.orderitem_set.all()

        cartItems=order.get_cart_items
    else:
        items=[]
        order={'get_cart_total':0,
        'get_cart_items':0}
        cartItems=order.get_cart_items
    context={'items':items,'order':order,'cartItems':cartItems,'shipping':False}
    return render(request,'store/checkout.html',context=context)

def cart(request):
    if request.user.is_authenticated:
        customer=request.user.customer
        order,created=Order.objects.get_or_create(customer,complete=False)
        items=order.orderitem_set.all()
        cartItems=order.get_cart_items


    else:
        items=[]
        order={'get_cart_total':0,
        'get_cart_items':0}
        cartItems=order.get_cart_items


    context={'items':items,'order':order,'cartItems':cartItems,'shipping':False}

    return render(request,'store/cart.html',context=context)


def updateItem(request):
    data=json.loads(request.body)
    productId=data['productId']
    action=data['action']

    customer=request.user.customer 
    product=Product.objects.get(id=productId)
    
    order,created=Order.objects.get_or_create(customer=customer,complete=False)
    orderItem,created = OrderItem.objects.get_or_create(order=order,product=product)
    
    if action == 'add':
        orderItem.quantity+=1
    elif action =='remove':
        orderItem.quantity-=1

    orderItem.save()


    if orderItem.quantity<=0:
        orderItem.delete()


    return JsonResponse('Item was added',safe=False)


def processOrder(request):
    transaction_id=datetime.datetime.now().timestamp()
    data=json.loads(request.body)

    if request.user.is_authenticated:
      
        customer=request.user.customer 
        order,created = Order.objects.get_or_create(customer=customer,complete=False)
        total=float(data['form']['total'])
        order.transaction_id = transaction_id

        if total ==order.get_cart_total:
       
            order.complete=True
           
        order.save()

        if order.shipping==True:
           
            Shipping.objects.create(customer=customer,address=data['shipping']['address'],
                                    zipcode=data['shipping']['zipcode'], city=data['shipping']['city'],
                                    state=data['shipping']['state'])

    return JsonResponse('Payment submitted',safe=False)