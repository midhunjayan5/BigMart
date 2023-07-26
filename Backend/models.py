from django.db import models

# Create your models here.
class categorydb(models.Model):
    catname=models.CharField(max_length=100,null=True,blank=True)
    description=models.CharField(max_length=100,null=True,blank=True)
    image=models.ImageField(upload_to="category Image")


class productdata(models.Model):
    category=models.CharField(max_length=100,null=True,blank=True)
    productname=models.CharField(max_length=100,null=True,blank=True)
    price=models.IntegerField(null=True,blank=True)
    description=models.CharField(max_length=100,null=True,blank=True)
    image=models.ImageField(upload_to="product",null=True,blank=True)


class Checkoutdb(models.Model):
    name=models.CharField(max_length=100,null=True,blank=True)
    email=models.EmailField(max_length=100,null=True,blank=True)
    address=models.CharField(max_length=100,null=True,blank=True)
    phone=models.IntegerField(null=True,blank=True)





