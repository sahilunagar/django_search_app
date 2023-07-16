from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('verify-otp', views.verify_otp, name='verify_otp')
]