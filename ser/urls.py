from django import views
from django.urls import path 
from . import views 
urlpatterns = [
    path('serv/',views.services,name='services') , 
]
