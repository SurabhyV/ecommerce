from django.urls import path
from . import views

urlpatterns=[
    path("CartDetails",views.Cart_detail,name='CartDetails'),
    path('add/<int:product_id>/',views.addcart,name='addcart'),
    path('cart_decrement/<int:product_id>/', views.min_cart, name='cart_decrement'),
    path('cart_delete/<int:product_id>/', views.cart_delete, name='delete'),
    path('pay/',views.payment,name='payment'),

]