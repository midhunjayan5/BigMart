from django.urls import path
from frontend import views



urlpatterns=[
    path('homepage/',views.homepage,name="homepage"),
    path('aboutpage/',views.aboutpage,name="aboutpage"),
    path('contactpage/',views.contactpage,name="contactpage"),
    path('productpage/<cat_name>',views.productpage,name="productpage"),
    path('singleproduct/<int:pro_id>',views.singleproduct,name="singleproduct"),
    path('',views.registration_page,name="registration_page"),
    path('save_registration/',views.save_registration,name="save_registration"),
    path('Userlogin/',views.Userlogin,name="Userlogin"),
    path('UserLogout/',views.UserLogout,name="UserLogout"),
    path('savecart/',views.savecart,name="savecart"),
    path('display_cart/',views.display_cart,name="display_cart"),
    path('delete_Cart/<int:cartid>',views.delete_Cart,name="delete_Cart"),
    path('checkoutpage/', views.checkoutpage, name="checkoutpage"),
    path('save_checkout/', views.save_checkout, name="save_checkout"),
    ]

