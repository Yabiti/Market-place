from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

app_name = 'sell'

urlpatterns = [
    path('', views.index, name='index'),
    path('contact', views.contact, name='contact'),
    path('signup/', views.signup, name='signup'),
 
]