from django.db import models
from django.template.defaultfilters import slugify
from  django.urls import reverse
# Create your models here.
class categ(models.Model):
     name=models.CharField(max_length=250,unique=True)
     slug=models.SlugField(max_length=250,unique=True)
     class Meta:
            ordering=('name',)
            verbose_name='category'
            verbose_name_plural='categories'
     def get_url(self):
         return reverse('prod_cat',args=[self.slug])
     def __str__(self):
          return '{}'.format(self.name)

class products(models.Model):
     name=models.CharField(max_length=250,unique=True)
     slug=models.SlugField(max_length=250,unique=True)
     img=models.ImageField(upload_to='product')
     desc=models.TextField()
     stock=models.IntegerField()
     available=models.BooleanField()
     price=models.IntegerField()
     category=models.ForeignKey(categ,on_delete=models.CASCADE)

     class Meta:
            ordering=('name',)
            verbose_name='product'
            verbose_name_plural='products'

     def get_urls(self):#function name can be any name
         return reverse('details',args=[self.category.slug,self.slug]) #here we need to get two arguments one is slug of category
     # another one is slug of the product table itself........from this function we call the url named 'item' where we need to get the
     #slug of the category and slug of product
     def __str__(self):
          return '{}'.format(self.name)

