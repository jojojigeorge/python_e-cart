from django.shortcuts import render,redirect
from store.models import Product,Cart,Order,OrderItem,Profile
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages


def orderdetails(request):
    order = Order.objects.filter(user=request.user)
    context = {'order':order}
    return render(request,"store/order/orderdetails.html",context)

def displayorder(request,t_no):
    order = Order.objects.filter(tracking_no=t_no).filter(user=request.user).first()
    orderitem =OrderItem.objects.filter(order=order)
    context = { 'order':order,'orderitem':orderitem}
    return render(request,'store/order/displayorder.html',context)

