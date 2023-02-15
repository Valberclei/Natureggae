from django.contrib.auth import views
from django.urls import path
from core_01.views import frontpage, shop, signup, myaccount, edit_myaccount, buscar_cidade
from product.views import product


urlpatterns = [
    path('buscar_cidade', buscar_cidade, name='buscar_cidade'),
    path('signup/', signup, name='signup'),
    path('logout_02/', views.LogoutView.as_view(), name='logout_02'),
    path('login_02/', views.LoginView.as_view(template_name='core_01/login_02.html'), name='login_02'),
    path('myaccount/', myaccount, name='myaccount'),
    path('myaccount/edit/', edit_myaccount, name='edit_myaccount'),
    path('frontpage', frontpage, name='frontpage'),
    path('shop/', shop, name='shop'),
    path('shop/<slug:slug>/', product, name='product'),
]