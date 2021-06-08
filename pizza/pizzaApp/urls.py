
from django.contrib import admin
from django.urls import path
from .views import acceptorder, declineorder, adminorders, userorders, placeorder, userlogout, userauthenticate, customerwelcomeview, userloginview, adminLoginView, adminHomePageView, authenticateAdmin, logoutadmin, addpizza, deletepizza, homepageview, signupuser

urlpatterns = [
    path('admin/', adminLoginView, name="adminloginpage"),
    path('adminauthenticate/', authenticateAdmin),
    path('admin/homepage', adminHomePageView, name="adminhomepage"),
    path('adminlogout/', logoutadmin),
    path('addpizza/', addpizza),
    path('deletepizza/<int:pizzapk>/', deletepizza),
    path('', homepageview, name="homepage"),
    path('signupuser/', signupuser),
    path('loginuser/', userloginview, name="userloginpage"),
    path('customer/welcome/', customerwelcomeview, name="customerpage"),
    path('customer/authenticate/', userauthenticate),
    path('userlogout/', userlogout),
    path('placeorder/', placeorder),
    path('userorders/', userorders),
    path('adminorders/', adminorders),
    path('acceptorder/<int:orderpk>/', acceptorder),
    path('declineorder/<int:orderpk>/', declineorder)

]
