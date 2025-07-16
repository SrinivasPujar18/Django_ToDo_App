from django.http import HttpResponse #(1)... importing HttpResponse
from django.shortcuts import redirect, render    #(2)... importing redirect

from todo.models import Task    #(2)... importing Task class

#(1)... Create your views here.
def addTask(request):           #(1)... defining addTask func
    task = request.POST['task']       #(2)... storing 'POST'(html) of task(input name) in var task
    Task.objects.create(task=task)  #(2)... storing "todo/models.py" task value to var task
    return redirect('home')         #(2)... returning the task to homePage
    #return HttpResponse('The form is submitted')    #(1)... prints in server

