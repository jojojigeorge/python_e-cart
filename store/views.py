
from django.http import JsonResponse

from unicodedata import category
from django.shortcuts import render,redirect
from .models import Category, Product
from django.contrib import messages

# Create your views here.
def productsearch(request):
    if request.method =='POST':
        searchedterm=request.POST.get('searchbox')
        print(searchedterm)
        if searchedterm == '':
            return redirect(request.META.get('HTTP_REFERER'))
        else:
            searchedproduct=Product.objects.filter(name__contains=searchedterm).first()
            if searchedproduct:
                return redirect('collections/'+searchedproduct.category.slug + '/'+ searchedproduct.slug)
        return redirect(request.META.get('HTTP_REFERER'))

def home(request):
    trending = Product.objects.filter(trending=1)
    category=Category.objects.filter(status=0)
    context={
        'category':category,
        'trending':trending
        }
    return render(request,'store/layouts/index.html',context)

def productlistAjax(request):
    products = Product.objects.filter(status=0).values_list('name',flat=True)
    productList = list(products)
    return JsonResponse(productList,safe = False)

def collections(request):
    category=Category.objects.filter(status=0)
    context={'category':category}
    return render(request,'store/layouts/collections.html',context)

def collectionsviews(request,slug):
    if (Category.objects.filter(slug=slug,status=0)):
        products=Product.objects.filter(category__slug=slug)
        category_selected=Category.objects.filter(slug=slug).first()
        #print(category_selected , products)
        context={
            'products':products,
            'category_selected':category_selected        
                    }
        return render(request,'store/products/index.html',context)
    else:
        messages.warning(request,"broken link")
        return redirect ('collections')


def productDetails(request,cat_slug,pro_slug):
    if (Category.objects.filter(slug=cat_slug,status=0)):
        if(Product.objects.filter(slug=pro_slug,status=0)):
            products=Product.objects.filter(slug=pro_slug,status=0).first
            context={'products':products}
        else:
            messages.error(request,"No such category found")
            return redirect('collections')
    else:
        messages.error(request,"No such category found")
        return redirect('collections')
    return render(request,'store/products/productDetails.html',context)
