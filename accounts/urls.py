from django.urls import path
from . import views
from  cart import urls
urlpatterns=[
    path("login/",views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('customer/',views.customer,name='customer'),
    path('registration/',views.register,name='register'),
    path('del/<int:id>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update'),
    path('users/<int:id>/',views.users,name='users'),
    path('userdelete/<int:id>/',views.userdel,name='userdel'),
]