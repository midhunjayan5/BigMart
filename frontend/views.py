from django.shortcuts import render, redirect

from Backend.models import categorydb, productdata,Checkoutdb
from frontend.models import registration, Cartdb
from django.contrib import messages


def homepage(request):
    cat = categorydb.objects.all()
    return render(request, "home.html", {'cat': cat})


def aboutpage(request):
    cat = categorydb.objects.all()
    return render(request, "about.html", {'cat': cat})


def contactpage(request):
    cat = categorydb.objects.all()
    return render(request, "contact.html", {'cat': cat})


def productpage(request, cat_name):
    product = productdata.objects.filter(category=cat_name)
    cat = categorydb.objects.all()
    return render(request, "products.html", {"product": product, "cat": cat})


def singleproduct(request, pro_id):
    product = productdata.objects.get(id=pro_id)
    cat = categorydb.objects.all()
    return render(request, "single_product.html", {"product": product, "cat": cat})


def registration_page(request):
    return render(request, "registration_page.html")


def save_registration(request):
    if request.method == 'POST':
        na = request.POST.get("r_name")
        em = request.POST.get("r_email")
        mo = request.POST.get("r_mobile")
        pas = request.POST.get("r_pass")
        img = request.FILES["img"]
        obj = registration(name=na, email=em, mobile=mo, password=pas, image=img)
        obj.save()
        return redirect(registration_page)


def Userlogin(request):
    if request.method == "POST":
        uname = request.POST.get("username")
        pwd = request.POST.get("password")
        if registration.objects.filter(name=uname, password=pwd).exists():
            request.session["username"] = uname
            request.session["password"] = pwd
            return redirect(homepage)
        else:
            return redirect(registration_page)
    return redirect(registration_page)


def UserLogout(request):
    del request.session["username"]
    del request.session["password"]
    return redirect(registration_page)


def savecart(request):
    if request.method == 'POST':
        uname = request.POST.get("uname")
        pname = request.POST.get("pname")
        dsc = request.POST.get("dsc")
        qty = request.POST.get("qty")
        tprice = request.POST.get("tprice")
        obj = Cartdb(Username=uname, Productname=pname, Description=dsc, quantity=qty, Totalprice=tprice)
        obj.save()
        return redirect(homepage)


def display_cart(request):
    displayCart = Cartdb.objects.filter(Username=request.session['username'])

    total_price=0
    for i in displayCart:
        total_price=total_price+i.Totalprice

    return render(request, "displaycart.html", {"displayCart": displayCart,"total_price":total_price})


def delete_Cart(request, cartid):
    cart = Cartdb.objects.get(id=cartid)
    cart.delete()
    return redirect(display_cart)


def checkoutpage(request):
    displayCart = Cartdb.objects.filter(Username=request.session['username'])

    total_price = 0
    for i in displayCart:
        total_price = total_price + i.Totalprice

    return render(request,"checkoutpage.html", {"displayCart": displayCart,"total_price":total_price})


def save_checkout(request):
    if request.method=="POST":
        na=request.POST.get("name")
        em=request.POST.get("email")
        ad=request.POST.get("address")
        ph=request.POST.get("phone")
        obj=Checkoutdb(name=na,email=em,address=ad,phone=ph)
        obj.save()
        messages.success(request,"Order is Placed")
        return redirect(homepage)
