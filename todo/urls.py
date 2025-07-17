#(1)... created by meeeeeeeee

from django.urls import path    #(1)...
from . import views

urlpatterns = [
    #addTask
    path('addTask/', views.addTask, name='addTask'),      #(1)... 
    #mark_as_done url
    path('mark_as_done/<int:pk>/', views.mark_as_done, name='mark_as_done'),       #(2)... by primary key(pk) we use task and mark_as_done
    #mark_as_undone url
    path('mark_as_undone/<int:pk>/', views.mark_as_undone, name='mark_as_undone'),       #(3)... by primary key(pk) we use task and mark_as_undone
    #Edit feature
    path('edit_task/<int:pk>/', views.edit_task, name='edit_task'),      #(4)... by primary key(pk) we use task for edit in new html file 
    #delete feature
    path('delete_task/<int:pk>/', views.delete_task, name='delete_task'),      #(5)... by primary key(pk) we can delete task
]