import json
from .models import *


def cookiecart(request):
        try:
            cart = json.loads(request.COOKIES['cart'])
        except:
            cart = {}
        print('Cart :', cart)
        items = []
        oorder = {'get_cart_total': 0, 'get_item_total': 0}
        cartitems = oorder['get_item_total']
        for i in cart:
            try:
                cartitems += cart[i]['quantity']
                prod = product.objects.get(id=i)
                total = (prod.price * cart[i]['quantity'])
                oorder['get_cart_total'] += total
                oorder['get_item_total'] += cart[i]['quantity']
                item = {
                    'product_id': {
                        'id': prod.id,
                        'title': prod.title,
                        'price': prod.price,
                        'imageURL': prod.imageURL,
                    },
                    'quantity': cart[i]['quantity'],
                    'get_total': total
                }
                items.append(item)
            except:
                pass
        oorder['get_total_with_del']=oorder['get_cart_total']+50

        return {'cartitems':cartitems ,'oorder':oorder, 'items':items}

def cartdata(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        oorder, created = order.objects.get_or_create(customer_id=customer,complete= False)
        items = oorder.ordered_item_set.all()
        cartitems = oorder.get_item_total
    else:
        cookiedata=cookiecart(request)
        cartitems=cookiedata['cartitems']
        oorder=cookiedata['oorder']
        items=cookiedata['items']
        customer={}

    
    return {'cartitems':cartitems ,'oorder':oorder, 'items':items,'customer':customer}

def guestorder(request,data):
    print('COOKIES',request.COOKIES)
    name=data['form']['name']
    email=data['form']['email']
    cookiedata= cookiecart(request)
    items= cookiedata['items']
    customerr, created = customer.objects.get_or_create(email_id=email)
    customerr.name=name
    customerr.save()
    oorder = order.objects.create(customer_id=customerr,complete=False)
    for item in items:
        product_id=product.objects.get(id=item['product_id']['id'])

        orderitem=ordered_item.objects.create(
            product_id=product_id,
            order_number=oorder,
            quantity=item['quantity']
            )
    return customerr,oorder
