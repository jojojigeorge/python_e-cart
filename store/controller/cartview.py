from django.shortcuts import render,redirect
from store.models import Product,Cart
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required


def deleteCartItem(request):
    if request.method=="POST":
        prod_id=int(request.POST.get('product_id'))
        if (Cart.objects.filter(user=request.user.id,product_id=prod_id)):
            cart= Cart.objects.get(product_id=prod_id,user=request.user)
            cart.delete()
            return JsonResponse({'status':" cart item deleted"})
    else:
        return redirect('/')


def updatecart(request):
    
    if request.method=="POST":
        prod_id=int(request.POST.get('product_id'))
        if (Cart.objects.filter(user=request.user.id,product_id=prod_id)):
            prod_qty=int(request.POST.get('product_qty'))
            cart= Cart.objects.get(product_id=prod_id,user=request.user)
            cart.product_qty = prod_qty
            cart.save()
            return JsonResponse({'status':"quantity updated"})
    else:
        return redirect('/')

@login_required(login_url='loginpage')
def createcart(request):
    
    cartitem=Cart.objects.filter(user=request.user)
    context={'cartitem':cartitem }
    return render(request,'store/products/createcart.html',context)

def addtocart (request):
    if request.method=="POST":
        if request.user.is_authenticated:
            prod_id=int(request.POST.get('product_id'))
            product_check=Product.objects.get(id=prod_id)
            if(product_check):
                if (Cart.objects.filter(user=request.user.id,product_id=prod_id)):
                    return JsonResponse({'status':"product alredy in cart"})
                else:
                    prod_qty=int(request.POST.get('product_qty'))
                    if product_check.quantity >= prod_qty:
                        
                        Cart.objects.create(user=request.user,product_id=prod_id,product_qty=prod_qty)
                        return JsonResponse({'status':"poduct added successfuly"})
                    else:
                        return JsonResponse({'status':"only some product remains"})

            else:
                return JsonResponse({'status':"No such product exist"})

        else:
            return JsonResponse({'status':"Login to continue"})

    return redirect('/')