from django.shortcuts import render,get_object_or_404,redirect
from .models import *
from django.conf import settings
from django.db.models import Q
from django.core.paginator import Paginator,EmptyPage,InvalidPage,PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login as auth_log,logout

# Create your views here.
@login_required(login_url='/accounts/login/')
def home(request,c_slug=None):
    if request.user.is_authenticated:
        c_catg = None
        prodt = None
        if c_slug != None:
            c_catg = get_object_or_404(categ, slug=c_slug)
            prodt = products.objects.filter(category=c_catg, available=True)
        else:

            prodt = products.objects.all().filter(available=True)
        cat = categ.objects.all()
        paginator = Paginator(prodt, 6)
        page = request.GET.get('page', '1')
        try:
            pro = paginator.page(page)
        except PageNotAnInteger:
            pro = paginator.page(1)
        except (EmptyPage, InvalidPage):
            pro = paginator.page(paginator.num_pages)
        return render(request, 'index.html', {'pr': prodt, 'ct': cat, 'pg': pro, 'page': page})
    else:
        return render(request,'login.html')

def basic(request):  # added extra to make category diaplayed on base.html
    categg=categ.objects.all()
    return render(request,'base.html',{'ct':categg})
@login_required(login_url='/accounts/login/')
def ProdDetails(request,c_slug,product_slug):
    if request.user.is_authenticated:
        try:
            prodt = products.objects.get(category__slug=c_slug,
                                         slug=product_slug)  # here we are using a try block,in that we are getting the product from the product table ie,
            # 'products' table .'objects' ie all products.. from that get, where category__slug=c_slug(product table we have a variable named category,which is actually the foreign key [primary key of category])
            # and slug of that table as product_slug.Here refering the category of table(product) we should use double undersqure( __ )

        except Exception as e:  # if error occured raise the exception
            raise e
        return render(request, 'item.html', {'pr': prodt})
    else:
        return request(request,'index.html')
def search(request):
    prod=None
    query=None
    if 'q' in request.GET:
        query=request.GET.get('q')
        prod=products.objects.all().filter(Q(name__contains=query)|Q(desc__contains=query)|Q(price__contains=query))
        return render(request, 'search.html', {'qr': query, 'pr': prod})
    else:
        return render(request,'notfound.html')