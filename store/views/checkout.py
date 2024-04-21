from django.shortcuts import render, redirect

from django.contrib.auth.hashers import check_password
from store.models.customer import Customer
from django.views import View

from store.models.product import Product
from store.models.orders import Order


class CheckOut(View):
    def post(self, request):
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        customer = request.session.get('customer')
        cart = request.session.get('cart')
        products = Product.get_products_by_id(list(cart.keys()))
        no_of_prods=len(products)
        orders=Order.get_orders_by_customer(customer)
        # print(orders)
        no_of_order=0
        pending_payment=0
        for order in orders:
            if order.status==False:
                pending_payment+=(order.price*order.quantity)
                no_of_order+=order.quantity  # no of orders already placed
        # print(pending_payment)
        checkout_price=0

        message=None
        error=False
        for product in products:
            # print(f'qty: {cart.get(str(product.id))}')
            checkout_price+=(product.price*cart.get(str(product.id)))
            no_of_order+=cart.get(str(product.id))  # no of orders being placed
        
        print(pending_payment+checkout_price)
        print(no_of_order)

        if no_of_prods==0:
            message="   Unable to Check-Out!"
            error=True
            return render(request , 'cart.html' , {'message' : message,'error':error} )      


        if no_of_order>10 or (pending_payment+checkout_price)>2000000:
            message="   Maximum 10 products can be booked at a time and total price should be less than Rs.20,00,000 (including Pending Orders)"
            error=True
            return render(request , 'cart.html' , {'message' : message,'error':error,'products':products} )

        
        else:
            for product in products:

                # print(cart.get(str(product.id)))
                order = Order(customer=Customer(id=customer),
                            product=product,
                            price=product.price,
                            address=address,
                            phone=phone,
                            quantity=cart.get(str(product.id)))
                order.save()
                message="   Order Placed!"

            request.session['cart'] = {}
            return render(request , 'cart.html' , {'message' : message,'error':error} )

         