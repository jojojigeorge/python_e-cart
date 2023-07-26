
from django.urls import path
from .import views
from  store.controller import authview,cartview,wishlistview,checkview,orderview

urlpatterns=[
    path('',views.home,name='home'),
    path('collections',views.collections,name='collections'),
    path('collections/<str:slug>',views.collectionsviews,name='collectionsviews'),
    path('collections/<str:cat_slug>/<str:pro_slug>',views.productDetails,name='productDetails'),
    
    path('product-list',views.productlistAjax),
    path('productsearch',views.productsearch,name='productsearch'),


    path('register/',authview.register,name='register'),
    path('login/',authview.loginpage,name='loginpage'),
    path('logout/',authview.logoutpage,name='logoutpage'),

    path('addtocart',cartview.addtocart,name='addtocart'),
    path('cart',cartview.createcart,name='createcart'),
    path('update-cart',cartview.updatecart,name='updatecart'),
    path('delete-cart-item',cartview.deleteCartItem,name='deleteCartItem'),

    path('wishlist',wishlistview.createwishlist,name='wishlist'),
    path('add_to_wishlist',wishlistview.addtowishlist,name='addtowishlist'),
    path('deletewishlist',wishlistview.deletewishlist,name='deletewishlist'),

    path('checkout',checkview.checkoutpage,name='checkout'),
    path('placeorder',checkview.placeorder,name='placeorder'),

    path('orderdetails',orderview.orderdetails,name='orderdetails'),
    path('display-order/<str:t_no>',orderview.displayorder,name='displayorder'),
    ]
    