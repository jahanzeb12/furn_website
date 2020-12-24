from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import JsonResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
import json
import datetime
from .models import *
from .forms import *
from .utils import *

# Create your views here.


def home(request):
    data=cartdata(request)
    cartitems=data['cartitems']
    oorder=data['oorder']
    items=data['items']

    context = {'items': items, 'oorder': oorder, 'cartitems': cartitems}
    return render(request, 'furnapp/index.html', context)


def products(request):
    data=cartdata(request)
    cartitems=data['cartitems']
        
    products = product.objects.all()
    context = {'products': products, 'cartitems': cartitems,'msgg':'ALL PRODUCTS'}

    return render(request, 'furnapp/products.html', context)

def searchMatch(query,item):
    if query in item.description.lower() or query in item.title.lower() or query in item.category.category.lower():
        return True
    else:
        return False

def search(request):
    search=request.GET.get('search')
    data=cartdata(request)
    cartitems=data['cartitems']
    products = product.objects.all()
    prod = [item for item in products if searchMatch(search, item)]
    n=len(prod)
    if(n>0):
        context={'products':prod, 'cartitems': cartitems,'msg':''}
    else:
        context={'products':products, 'cartitems': cartitems,'msg':"Write the correct query, item not matched"}
    return render(request, 'furnapp/products.html', context)


def about(request):
    data=cartdata(request)
    cartitems=data['cartitems']
        
    context = {'cartitems': cartitems}
    return render(request, 'furnapp/about.html', context)


def contact(request):
    data=cartdata(request)
    cartitems=data['cartitems']
    form =contactform()
    if request.method=='POST':
         form =contactform(request.POST)
         if form.is_valid():
            form.save()
            

        
    context = {'cartitems': cartitems,'form':form}
    return render(request, 'furnapp/contact.html', context)


def productsdet(request, product_name):

    product_det = product.objects.get(title=product_name)
    form = commentform()
    if request.method == 'POST':
        form = commentform(request.POST)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.Product=product_det
            instance.save()
   
    
    data=cartdata(request)
    cartitems=data['cartitems']
    revi=review.objects.filter(Product=product_det.id)   

    context = {'product_det': product_det,
               'cartitems': cartitems ,'form':form,'review':revi}

    return render(request, 'furnapp/product_details.html', context)

def category(request, category_n):
    products= product.objects.filter(category=category_n)
    data=cartdata(request)
    cartitems=data['cartitems']
    msg=products[0].category
    context={'products':products,'cartitems': cartitems,'msgg':msg}
    return render(request, 'furnapp/products.html', context)


def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            
            messages.success(request, 'Account was succesfully created')
            username = form.cleaned_data['username']
            raw_password = form.cleaned_data['password1']
            user = authenticate(username=username, password=raw_password)
            custom, created = customer.objects.get_or_create(user=user)
            login(request, user)

            return render(request, 'furnapp/index.html')

    context = {'form': form}
    return render(request, 'furnapp/register.html', context)


def cart(request):
    
    data=cartdata(request)
    cartitems=data['cartitems']
    oorder=data['oorder']
    items=data['items']

    context = {'items': items, 'oorder': oorder, 'cartitems': cartitems}
    return render(request, 'furnapp/cart.html', context)


def checkout(request):
    data=cartdata(request)
    cartitems=data['cartitems']
    oorder=data['oorder']
    items=data['items']
    customer=data['customer']

    context = {'items': items, 'oorder': oorder,'cartitems': cartitems, 'customer': customer}
    return render(request, 'furnapp/checkout.html', context)


def update_item(request):
    data = json.loads(request.body)
    productid = data['productid']
    action = data['action']
    print(productid)
    print(action)
    customerr = request.user.customer
    Product = product.objects.get(id=productid)
    oorder, created = order.objects.get_or_create(customer_id=customerr,complete=False)
    orderitem, created = ordered_item.objects.get_or_create(
        order_number=oorder, product_id=Product)
    if action == 'add':
        orderitem.quantity += 1
        Product.quantity -=1
    elif action == 'remove':
        orderitem.quantity -= 1
        Product.quantity +=1
    elif action == 'add_cart':
        if(orderitem.quantity == 0):
            orderitem.quantity += 1
            Product.quantity -=1

    orderitem.save()
    Product.save()
    if orderitem.quantity <= 0:
        orderitem.delete()
    if Product.quantity <= 0:
        Product.delete()

    return JsonResponse('im here', safe=False)

def processorder(request):
    transaction_id=datetime.datetime.now().timestamp()
    data=json.loads(request.body)
    name=data['form']['name']
    email=data['form']['email']
    if request.user.is_authenticated:
        customerr = request.user.customer
        oorder, created = order.objects.get_or_create(customer_id=customerr,complete=False)
        
        customerr.name=name
        customerr.email_id=email
        customerr.save()
        
        
    else:
        customerr,oorder = guestorder(request,data)
    
    total = float(data['form']['total'])
    oorder.transaction_id=transaction_id
    if total == oorder.get_cart_total:
        oorder.complete= True
    oorder.save()
    shipping.objects.create(
		customer=customerr,
		order=oorder,
		address=data['shipping']['address'],
		city=data['shipping']['city'],
		country=data['shipping']['state'],
		zipcode=data['shipping']['zipcode'],
        contact_no=data['shipping']['contact_no']
		)

    return JsonResponse('transaction complete', safe=False)