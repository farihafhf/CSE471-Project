# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('create_project/', views.create_project, name='create_project'),
    path('project/<int:project_id>/', views.project_page, name='project_page'),
    path('create_task/<int:project_id>/', views.create_task, name='create_task'),
    path('delete_task/<int:task_id>/', views.delete_task, name='delete_task'),
    path('task_page/', views.task_page, name='task_page'),
]