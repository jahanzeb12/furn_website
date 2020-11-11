from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout


# Create your views here.
from .forms import CreateUserForm

def home(request):
    return render(request,'furnapp/index.html')

def products(request):
    return render(request,'furnapp/products.html')

def about(request):
    return render(request,'furnapp/about.html')

def contact(request):
    return render(request,'furnapp/contact.html')

def productsdet(request):
    return render(request,'furnapp/product_details.html')

def loginpage(request):
    
    if request.method=='POST':
        username = request.POST.get('username')
        password =request.POST.get('password')
        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            print('kuch bhi')
            return redirect('main')
        else:
            messages.info(request,'username not')
            print('kuch bhi 1')
            

    context = {}
    return render(request,'furnapp/login.html',context)

def register(request):
    form = CreateUserForm()
    if request.method =='POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Account was succesfully created')
            username = form.cleaned_data['username']
            raw_password = form.cleaned_data['password1']
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            
            return render(request,'furnapp/index.html')

    
    context = {'form': form}
    return render(request,'furnapp/register.html',context)

    
