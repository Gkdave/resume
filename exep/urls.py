from django.urls import path 
from . import views 

urlpatterns = [
    path('exep/',views.experience,name='exep'),
]
