from django.shortcuts import render , redirect,HttpResponse

from django.contrib.auth.hashers import  check_password
from store.models.customer import Customer
from django.views import  View
from store.models.product import  Product

class Cart(View):
    def post(self,request):
        product = request.POST.get('product')#will get product id when add to cart is clicked with name product
        remove = request.POST.get('remove') #remove is a name for - in home
        cart = request.session.get('cart')

        if cart:  # checking if cart already exists or not
            quantity = cart.get(product)
            if quantity:   # if the product exists in cart 
                if remove:
                    if quantity<=1:
                        cart.pop(product)  # remove item of key product from cart dictionary
                    else:
                        cart[product]  = quantity-1
                else:
                    cart[product]  = quantity+1

            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1

        request.session['cart'] = cart
        ids = list(request.session.get('cart').keys())
        products = Product.get_products_by_id(ids) # it is defined in products.py modles
        # print(products)
        return render(request , 'cart.html' , {'products' : products} )
    

    def get(self , request):
        ids = list(request.session.get('cart').keys())
        products = Product.get_products_by_id(ids) # it is defined in products.py modles
        # print(products)
        return render(request , 'cart.html' , {'products' : products} )

