from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib import messages

from Backend.models import categorydb, productdata


# Create your views here.
def indexpage(request):
    return render(request, "index.html")


def addcategory(request):
    return render(request, "Add_category.html")


def savecategory(request):
    if request.method == "POST":
        na = request.POST.get("c_name")
        des = request.POST.get("c_des")
        img = request.FILES["c_image"]
        obj = categorydb(catname=na, description=des, image=img)
        obj.save()
        messages.success(request,"Category added Successfully")
        return redirect(addcategory)


def display_cat(request):
    cat = categorydb.objects.all()
    return render(request, "displaycategory.html", {"cat": cat})


def editcat(request, catid):
    cat = categorydb.objects.get(id=catid)
    return render(request, "edit_category.html", {"cat": cat})


def update_cat(request, catid):
    if request.method == "POST":
        na = request.POST.get("c_name")
        des = request.POST.get("c_des")
    try:
        img = request.FILES["c_image"]
        fs = FileSystemStorage()
        file = fs.save(img.name, img)
    except MultiValueDictKeyError:
        file = categorydb.objects.get(id=catid).image
    categorydb.objects.filter(id=catid).update(catname=na, description=des, image=file)
    return redirect(display_cat)


def delete_cat(request, catid):
    cat = categorydb.objects.get(id=catid)
    cat.delete()
    return redirect(display_cat)


def add_products(request):
    cat = categorydb.objects.all()
    return render(request, "Add_products.html", {"cat": cat})


def save_product(request):
    if request.method == "POST":
        cname = request.POST.get("c_name")
        pna = request.POST.get("p_name")
        pri = request.POST.get("p_price")
        des = request.POST.get("p_des")
        img = request.FILES["p_image"]
        obj = productdata(category=cname, productname=pna, price=pri, description=des, image=img)
        obj.save()
        messages.success(request,"Products Added Successfully")
    return redirect(add_products)


def display_products(request):
    product = productdata.objects.all()
    return render(request, "display_products.html", {"product": product})


def deleteproduct(request, proid):
    product = productdata.objects.get(id=proid)
    product.delete()
    return redirect(display_products)


def editproduct(request,proid):
    product=productdata.objects.get(id=proid)
    return render(request,"edit_product.html",{"product":product})

def updateproduct(request,proid):
    if request.method == "POST":
        cname = request.POST.get("c_name")
        pna = request.POST.get("p_name")
        pri = request.POST.get("p_price")
        des = request.POST.get("p_des")

    try:
        img = request.FILES["p_image"]
        fs = FileSystemStorage()
        file = fs.save(img.name, img)
    except MultiValueDictKeyError:
        file = productdata.objects.get(id=proid).image
    productdata.objects.filter(id=proid).update(category=cname, productname=pna,price=pri,description=des, image=file)
    return redirect(display_products)


def loginpage(request):
    return render(request,"loginpage.html")

def adminlogin(request):
    if request.method=='POST':
        uname=request.POST.get("username")
        pwd=request.POST.get("password")
        if User.objects.filter(username__contains=uname).exists():
            user=authenticate(username=uname,password=pwd)
            if user is not None:
                login(request,user)
                request.session["username"]=uname
                request.session["password"]=pwd
                messages.success(request,"Sucessfully Log In")
                return redirect(indexpage)
            else:
                messages.error(request,"invalid Username or Password")
                return redirect(loginpage)
        else:
            messages.error("invalid Username or Password")
            return redirect(loginpage)


def logoutadmin(request):
    del request.session["username"]
    del request.session["password"]
    return redirect(loginpage)

