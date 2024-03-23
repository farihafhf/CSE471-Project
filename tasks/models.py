from django.db import models
from django.contrib.auth.models import User


class Project(models.Model):
    project_id = models.AutoField(primary_key=True)  
    project_name = models.CharField(max_length=100)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)  
    created_at = models.DateTimeField(auto_now_add=True)
    collaborators = models.ManyToManyField(User, related_name='collaborating_projects', blank=True)
    
    def __str__(self):
        return self.project_name

class Task(models.Model):
    task_id = models.AutoField(primary_key=True) 
    task_name = models.CharField(max_length=100)
    parent_project = models.ForeignKey(Project, on_delete=models.CASCADE)
    completion = models.BooleanField(default=False)  
    description = models.TextField(default="")  # Providing a default value
    time = models.IntegerField(default=0)
    PRIORITY_CHOICES = (
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
    ) 

    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='Low')
    deadline = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.task_name




class Notice(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None, null=True, blank=True)
    notice = models.TextField(default="End", null=True, blank=True)
    task = models.ForeignKey(Task, on_delete=models.CASCADE,default=None, null=True, blank=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, default=None, null=True, blank=True)  # Allow NULL values
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='assigned_tasks', blank=True, null=True)
    
    def __str__(self):
        return f"{self.user.username} - {self.notice}"
    







