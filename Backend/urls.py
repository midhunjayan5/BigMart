from django.urls import path
from Backend import views



urlpatterns=[
    path('addcategory/',views.addcategory,name="addcategory"),
    path('indexpage/',views.indexpage,name="indexpage"),
    path('savecategory/',views.savecategory,name="savecategory"),
    path('display_cat/',views.display_cat,name="display_cat"),
    path('editcat/<int:catid>',views.editcat,name="editcat"),
    path('update_cat/<int:catid>',views.update_cat,name="update_cat"),
    path('delete_cat/<int:catid>',views.delete_cat,name="delete_cat"),
    path('add_products/',views.add_products,name="add_products"),
    path('save_product/',views.save_product,name="save_product"),
    path('display_products/',views.display_products,name="display_products"),
    path('deleteproduct/<int:proid>',views.deleteproduct,name="deleteproduct"),
    path('editproduct/<int:proid>', views.editproduct, name="editproduct"),
    path('updateproduct/<int:proid>', views.updateproduct, name="updateproduct"),
    path('loginpage/', views.loginpage, name="loginpage"),
    path('adminlogin/', views.adminlogin, name="adminlogin"),
    path('logoutadmin/', views.logoutadmin, name="logoutadmin"),

]