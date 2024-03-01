from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    project_id = models.AutoField(primary_key=True)  
    project_name = models.CharField(max_length=100)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)  
    created_at = models.DateTimeField(auto_now_add=True) 

from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    project_id = models.AutoField(primary_key=True)  
    project_name = models.CharField(max_length=100)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)  
    created_at = models.DateTimeField(auto_now_add=True) 

class Task(models.Model):
    task_id = models.AutoField(primary_key=True) 
    task_name = models.CharField(max_length=100)
    parent_project = models.ForeignKey(Project, on_delete=models.CASCADE)
    completion = models.BooleanField(default=False)  




