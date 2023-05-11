from django.shortcuts import render,redirect,HttpResponseRedirect,reverse,get_object_or_404
from django.contrib.auth.forms import UserCreationForm

from shop.models import products
from .forms import CreateUserForm,Productorder,Userdetl
from django.contrib import messages, auth
from shop import urls
from django.contrib.auth import authenticate,login as auth_log,logout
from django.contrib.auth.decorators import login_required
from cart.views import *
from django.contrib.auth.models import User
# Create your views here.
def login(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth_log(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Username and Password doesnot match')
        return render(request,'login.html')

def logout(request):
        auth.logout(request)
        return redirect('/')
    # if request.user.is_authenticated:
        # auth.logout(request,user)
        # return render(request,'login.html')
    # else:
    #     return redirect('home')
def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()

        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save();
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account created :' + user)
                return redirect('login')
        return render(request,'registration.html',{'form':form})

def dashboard(request):
    customer=User.objects.all()
    prodt = products.objects.all().filter(available=True)
    return render(request,'dashboard.html',{'pr':prodt,'cus':customer})

def customer(request):
    return render(request,'customer_detail.html')

def delete(request,id):
    prod = products.objects.get(id=id)
    prod.delete()
    return redirect('dashboard')
def update(request,id):
    prod=products.objects.get(id=id)
    form=Productorder(instance=prod)
    if request.method=='POST':
        form=Productorder(request.POST,instance=prod)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    return render(request,'update.html',{'form':form})

def users(request,id):
    user=User.objects.get(id=id)
    form=Userdetl(instance=user)#getting user value on corresponding fields and passing this form as ginga format to html template
    if request.method == 'POST':
        form = Userdetl(request.POST, instance=user)

        if form.is_valid():
            form.save()
            return redirect('dashboard')
    return render(request, 'user.html', {'form': form,'id':user})
def userdel(request,id):
    user=User.objects.get(id=id)
    user.delete()
    return redirect('dashboard')