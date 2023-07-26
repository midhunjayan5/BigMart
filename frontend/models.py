from django.db import models

# Create your models here.
class registration(models.Model):
    name=models.CharField(max_length=100,null=True,blank=True)
    email=models.EmailField(null=True,blank=True)
    mobile=models.CharField(max_length=100,null=True,blank=True)
    password=models.CharField(max_length=100,null=True,blank=True)
    image=models.ImageField(upload_to="registration",null=True,blank=True)


class Cartdb(models.Model):
    Username=models.CharField(max_length=100,null=True,blank=True)
    Productname=models.CharField(max_length=100,null=True,blank=True)
    Description=models.CharField(max_length=100,null=True,blank=True)
    quantity=models.IntegerField(null=True,blank=True)
    Totalprice=models.IntegerField(null=True,blank=True)


