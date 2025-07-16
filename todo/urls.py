#(1)... created by meeeeeeeee

from django.urls import path    #(1)...
from . import views

urlpatterns = [
    path('addTask/', views.addTask, name='addTask'),      #(1)... 
]