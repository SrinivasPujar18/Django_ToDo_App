#...(1) created by meeeeeeee
#from django.http import HttpResponse      #...(2) importing HttpResponse 
from django.shortcuts import render        #...(3) importing render


def home(request):
    #... return HttpResponse('<h2> HomePage </h2>')         #...(2) printing in server from HttpResponse
    return render(request,'home.html')                      #...(3) rendering the request from 'home.html' file
