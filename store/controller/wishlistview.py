from django.shortcuts import render,redirect
from django.contrib import messages
from store.models import Product,Cart,Wishlist
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

@login_required(login_url='loginpage')
def createwishlist(request):
    wishlistitem=Wishlist.objects.filter(user=request.user)
    context={'wishlistitem':wishlistitem }
    return render(request,'store/products/wishlist.html',context)

    
def deletewishlist(request):
    if request.method=="POST":
        
        prod_id=int(request.POST.get('product_id'))
        if (Wishlist.objects.filter(user=request.user.id,product_id=prod_id)):
            wish= Wishlist.objects.get(product_id=prod_id,user=request.user)
            wish.delete()
            return JsonResponse({'status':" wishlist item deleted"})
    else:
        return redirect('/')

def addtowishlist(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            prod_id = int(request.POST.get('product_id'))
            product_check =Product.objects.get(id=prod_id)
            if (product_check):
                if(Wishlist.objects.filter(user=request.user,product_id=prod_id)):
                    return JsonResponse({'status':'Alredy in wishlist'})
                else:
                    Wishlist.objects.create(user=request.user,product_id=prod_id)
                    return JsonResponse({'status':"added to wishlist successfully"})
            else:
                return JsonResponse({'status':"No such product exist"})
        else:
            return JsonResponse({'status':'Login to continue'})
    return redirect('/')