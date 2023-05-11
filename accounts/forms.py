from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms
from shop.models import products
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields =['username','email','password1','password2']
class Productorder(ModelForm):
    class Meta:
        model=products
        fields=['name','slug','img','desc','stock','available','price','category']

class Userdetl(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']