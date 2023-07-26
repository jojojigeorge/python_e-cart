$(document).ready(function () {
    
    $('.increment-btn').click(function (e) { 
        e.preventDefault();
        var inc_value=$(this).closest('.product_data').find('.qty_input').val();
        var value = parseInt(inc_value,10);
        value=isNaN(value) ? 0 : value;
        if( value < 10 )
        {
            value++;
            $(this).closest('.product_data').find('.qty_input').val(value);

        }
    });



    $('.decrement-btn').click(function (e) { 
        e.preventDefault();
        var dec_value=$(this).closest('.product_data').find('.qty_input').val();
        var value = parseInt(dec_value,10);
        
        value=isNaN(value) ? 0 : value;
        if( value > 1 )
        {
            value--;
            $(this).closest('.product_data').find('.qty_input').val(value);

        }
    });
    $('.addToCartBtn' ).click(function (e) { 
        e.preventDefault();
        var product_id=$(this).closest('.product_data').find('.prod_id').val();
        var product_qty=$(this).closest('.product_data').find('.qty_input').val();
        var token=$('input[name=csrfmiddlewaretoken').val();
        
        $.ajax({
            method:"POST",
            url: "/addtocart",
            data: {
                'product_id':product_id,
                'product_qty':product_qty,
                csrfmiddlewaretoken:token
            },
            success: function (response) {
                alertify.success(response.status)
            }
        });
        
    });
    $('.changeQuantity' ).click(function (e) { 
        e.preventDefault();
        var product_id=$(this).closest('.product_data').find('.prod_id').val();
        var product_qty=$(this).closest('.product_data').find('.qty_input').val();
        var token=$('input[name=csrfmiddlewaretoken').val();
        
        $.ajax({
            method:"POST",
            url: "/update-cart",
            data: {
                'product_id':product_id,
                'product_qty':product_qty,
                csrfmiddlewaretoken:token
            },
           
            success: function (response) {
                alertify.success(response.status)
            }
        });
        
    });


    $(document).on('click','.delete-cart-item' ,function (e) {
        e.preventDefault();
        var product_id=$(this).closest('.product_data').find('.prod_id').val();
        var token=$('input[name=csrfmiddlewaretoken').val();
        console.log(product_id);
        $.ajax({
            method:"POST",
            url: "/delete-cart-item",
            data: {
                'product_id':product_id,
                csrfmiddlewaretoken:token
            },
           
            success: function (response) {
                alertify.success(response.status)
                $('.cartdiv').load(location.href + ' .cartdiv');
            }
        });
    });


    $(document).on('click','.delete-wishlist-item' ,function (e) {
        e.preventDefault();
        var product_id=$(this).closest('.product_data').find('.prod_id').val();
        var token=$('input[name=csrfmiddlewaretoken').val();
        console.log(product_id);
        $.ajax({
            method:"POST",
            url: "/deletewishlist",
            data: {
                'product_id':product_id,
                csrfmiddlewaretoken:token
            },
           
            success: function (response) {
                alertify.success(response.status)
                $('.wishlistdiv').load(location.href + ' .wishlistdiv');
            }
        });
    });


    $('.addToWishBtn').click(function (e) { 
        e.preventDefault();
        var product_id=$(this).closest('.product_data').find('.prod_id').val();
        var token = $('input[name=csrfmiddlewaretoken').val();
        $.ajax({
            
            method:"POST",
            url:'/add_to_wishlist',
            data: {
                'product_id': product_id,
                csrfmiddlewaretoken:token,
            },
            success: function (response) {
                alertify.success(response.status)
                
            }
        });
        
    });


   
});