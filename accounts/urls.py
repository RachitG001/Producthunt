from django.urls import path,include
from . import views

urlpatterns = [
    path('signup',views.signup,name='signup_page'),
    path('login',views.login,name='login_page'),
    path('logout',views.logout,name='logout_page'),
] 