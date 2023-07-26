from django.shortcuts import render,redirect
from store.models import Product,Cart,Order,OrderItem,Profile
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages

from django.http import JsonResponse


import random

@login_required(login_url='loginpage')
def     placeorder(request):
    if request.method == 'POST':
        #current_user = User.objects.filter(id=request.user).first()
        neworder=Order()
        neworder.user = request.user
        neworder.fname = request.POST.get('fname')
        neworder.lname = request.POST.get('lname')
        neworder.email = request.POST.get('email')
        neworder.phone = request.POST.get('phone')
        neworder.address = request.POST.get('address')
        neworder.city = request.POST.get('city')
        neworder.state= request.POST.get('state')
        neworder.country = request.POST.get('country')
        neworder.pincode = request.POST.get('pincode')
        neworder.payment_mode = request.POST.get('payment_mode')




        cart = Cart.objects.filter(user=request.user)
        cart_total = 0
        for i in cart:
            cart_total=cart_total+i.product_qty*i.product.selling_price
        neworder.total_price=cart_total

        trackno='TRN'+str(random.randint(1111111 ,9999999))
        while Order.objects.filter(tracking_no=trackno) is None:
            trackno='TRN'+str(random.randint(1111111 ,9999999))
        neworder.tracking_no = trackno
        neworder.save()


        if not Profile.objects.filter(user=request.user):
            userprofile=Profile()
            userprofile.user = request.user
            userprofile.order = neworder
            userprofile.save()

        neworderitems = Cart.objects.filter(user=request.user)
        for item in neworderitems:
            OrderItem.objects.create(
                order = neworder,
                product = item.product,
                price = item.product.selling_price,
                quantity = item.product_qty
            )

        #To decrese available quantity
        order_product = Product.objects.filter(id=item.product_id).first()
        order_product.quantity = order_product.quantity - item.product_qty
        order_product.save()


        #To clear user cart
        Cart.objects.filter(user=request.user).delete()


        # messages.success(request,"Your order has been placed successfuly")
    return redirect('orderdetails')


@login_required(login_url='loginpage')
def checkoutpage(request):
    rawcart = Cart.objects.filter(user=request.user)
    for item in rawcart:
        if item.product_qty > item.product.quantity:
            Cart.objects.delete(id=item.id)

    cartitem = Cart.objects.filter(user=request.user)
    total_price=0
    userprofile=Profile.objects.filter(user=request.user).first()
    for i in cartitem:
        total_price = total_price + (i.product.selling_price * i.product_qty)
    context={
        'userprofile':userprofile,
        'cartitem': cartitem,
        'total_price':total_price
    }
    return render(request,"store/checkout/checkoutIndex.html",context)