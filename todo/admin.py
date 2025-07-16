from django.contrib import admin
from .models import Task  #...(1) importing Task from current directory "models.py"

class TaskAdmin(admin.ModelAdmin):              #...(2) creating class TaskAdmin to show tasks info in server
    list_display =  ('task', 'is_completed', 'updated_at')   #(3)... list_display and search_fields are Attributes, we can add many
    search_fields = ('task',)                #(3)... this is must be list or tuple by(,)

admin.site.register(Task, TaskAdmin)            #...(1) Register your models here.        (2)... calling TaskAdmin class
