from django.urls import path
from . import views

urlpatterns = [
    path('home', views.Home, name="home"),
    path('accounts/login/', views.login_view, name="login"),
    path('accounts/register/', views.Register, name="register"),
    path('accounts/logout/', views.Logout, name="logout")
]
