from django.shortcuts import render , redirect,HttpResponse

from django.contrib.auth.hashers import  check_password
from store.models.customer import Customer
from django.views import  View
from store.models.product import  Product

class Cart(View):
    def get(self , request):
        ids = list(request.session.get('cart').keys())
        products = Product.get_products_by_id(ids) # it is defined in products.py modles
        # print(products)
        return render(request , 'cart.html' , {'products' : products} )

