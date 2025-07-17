from django.http import HttpResponse #(1)... importing HttpResponse
from django.shortcuts import get_object_or_404, redirect, render    #(2)... importing redirect       ()

from todo.models import Task    #(2)... importing Task class

#(1)... Create your views here.
def addTask(request):           #(1)... defining addTask func
    task = request.POST['task']       #(2)... storing 'POST'(html) of task(input name) in var task
    Task.objects.create(task=task)  #(2)... storing "todo/models.py" task value to var task
    return redirect('home')         #(2)... returning the task to homePage
    #return HttpResponse('The form is submitted')    #(1)... prints in server

def mark_as_done(request, pk):            #(3)...
    task = get_object_or_404(Task, pk=pk)    #(4)... getting task, if not it gives 404 error from Task with primary key(pk)
    task.is_completed = True               #(4)... if task is completed, if it's True then will respond
    task.save()                         #(4)... it saves the completed task
    return redirect('home')        #(4)... returning response of task in homePage
    #return HttpResponse(pk)     #(3)...

def mark_as_undone(request, pk):            #(5)...
    task = get_object_or_404(Task, pk=pk)    #(5)... getting task, if not it gives 404 error from Task with primary key(pk)
    task.is_completed = False              #(5)... if task is completed, if it's False then will respond
    task.save()                         #(5)... it saves the completed task
    return redirect('home')         #(5)...returning response of task in homePage


def edit_task(request, pk):            #(6)...
    get_task = get_object_or_404(Task, pk=pk)    #(6)... get_task is var
    if request.method == 'POST': #(6)... accessing POST
        #return  
        new_task = request.POST['task']   #(7)... 'task' is name of input line:38, it access to POST method                        
        get_task.task = new_task      #(7)... new_task assigning to get_task variable with "todo/models.py" task=""
        get_task.save()             #(7)... it saves the get_task
        return redirect('home')         #(7)... returning response of get_task in homePage
    else:
        context = {
            'get_task' : get_task
        }
    #return render(request, 'edit_task.html', context) #(6)... rendering the edit_task.html
        return render(request, 'edit_task.html', context) #(7)... rendering the edit_task.html


def delete_task(request, pk):              #(8)... declaring delete_task
    task = get_object_or_404(Task, pk=pk)   #(8)... task is var
    task.delete()    #(8)...built-in func delete
    return redirect('home')    #(8)... returning response of task in homePage
