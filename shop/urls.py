from . import views
from django.urls import path

urlpatterns=[
    path('',views.home,name='home'),
    path('<slug:c_slug>/',views.home,name='prod_cat'),
    path('<slug:c_slug>/<slug:product_slug>',views.ProdDetails,name='details'),
    path('search',views.search,name='search')
]

