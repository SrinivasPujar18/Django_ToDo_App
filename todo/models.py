from django.db import models

#...(1) Create your models here. And for assigning task in server
class Task(models.Model):                                  #...(1) defining class 'Task'
    task = models.CharField(max_length=250)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.task
