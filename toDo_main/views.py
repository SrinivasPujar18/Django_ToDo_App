#...(1) created by meeeeeeee
#from django.http import HttpResponse      #...(2) importing HttpResponse 
from django.shortcuts import render        #...(3) importing render
from todo.models import Task               #...(4) importing Task class


def home(request):
    #... return HttpResponse('<h2> HomePage </h2>')         #...(2) printing in server from HttpResponse
    tasks = Task.objects.filter(is_completed=False).order_by('-updated_at')   #...(4) Fetching tasks and show whether task is completed or not      (5)... we altered this line by adding order_by()
    context = {
        'tasks' : tasks,                                    #...(4) dict contains tasks
    }
    return render(request,'home.html', context)                      #...(3) rendering the request from 'home.html' file
