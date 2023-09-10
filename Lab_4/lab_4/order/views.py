from django.shortcuts import render
from .models import OrderItem
from cart.cart import Cart
from store.models import Client
from .models import Order
from django.core.exceptions import PermissionDenied


def order_create(request):
    if not request.user.is_authenticated :
        raise PermissionDenied("You do not have access to this page.")

    cart = Cart(request)
    if request.method == 'POST':
        order = Order.objects.create(client=Client.objects.filter(id=request.user.id).first())
        print(request.user.id)
        print(order.id)
        for item in cart:
            OrderItem.objects.create(order=order,
                                        product=item['product'],
                                        price=item['cost'],
                                        quantity=item['quantity'])
            item['product'].purchase_count += item['quantity']
            item['product'].save()

        # очистка корзины
        cart.clear()
        return render(request, 'order/created.html',
                        {'order': order})
    
    return render(request, 'order/create.html',
                  {'cart': cart})