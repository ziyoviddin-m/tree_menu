from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('contacts/', index, name='contacts'),
    path('our_projects/', our_projects, name='our_projects'),
    path('services/', index, name='services'),
    path('price/', index, name='price'),
    path('employees/', index, name='employees'),
    path('adres/', index, name='adres'),
    path('qwerty/', index, name='qwerty'),
    path('abcd/', index, name='abcd'),
    path('admin/', index, name='admin'),
    path('sdf/', index, name='sdf'),
]


