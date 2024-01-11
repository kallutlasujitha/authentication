from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('signup', signup, name='signup'),
    path('login/',login_view, name='login'),
    path('home/',home, name='home'),
    path('logout/',logout_view, name='logout'),
    path('delete/',delete_account, name='delete'),
]





