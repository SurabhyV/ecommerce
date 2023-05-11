from django.db import models
from shop.models import *
from django.contrib.auth.models import User
# Create your models here.
class cartlist(models.Model):
    user= models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    cart_id=models.CharField(max_length=250,unique=True)
    date=models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name='cartlist'
        verbose_name_plural='cartlists'

    def __str__(self):
         return str(self.cart_id)
class items(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    prodt=models.ForeignKey(products,on_delete=models.CASCADE)
    cart=models.ForeignKey(cartlist,on_delete=models.CASCADE)
    quan=models.IntegerField()

    class Meta:
        verbose_name = 'item'
        verbose_name_plural = 'items'

    def __str__(self):
        return str(self.prodt)#added an str

    def total(self):
        return str(self.prodt.price*self.quan)

