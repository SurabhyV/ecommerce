from django.contrib import admin
from .models import *
# Register your models here.
class catagdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
   
admin.site.register(categ,catagdmin)# should be in order ie,first table name(categ) and next class name(catagdmin)

class product(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    list_display = ['name','slug','img','stock','available','price','category']
    list_editable = ['img','stock','available','price','category']
admin.site.register(products,product)# should be in order ie,first table name(products) and next class name(product) otherwise error :TypeError: 'MediaDefiningClass' object is not iterable
