# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('create_project/', views.create_project, name='create_project'),
    path('project/<int:project_id>/', views.project_page, name='project_page'),
    path('create_task/<int:project_id>/', views.create_task, name='create_task'),
    path('delete_task/<int:task_id>/', views.delete_task, name='delete_task'),
    path('task_page/', views.task_page, name='task_page'),
    path('task/<int:task_id>/start/', views.start_timer, name='start_timer'),
    path('task/<int:task_id>/stop/', views.stop_timer, name='stop_timer'),
    path('task/<int:task_id>/reset/', views.reset_timer, name='reset_timer'),
    path('task/<int:task_id>/pause/', views.pause_timer, name='pause_timer'),
    path('delete_project/<int:project_id>/', views.delete_project, name='delete_project'),
    path('back_to_dashboard/', views.back_to_dashboard, name='back_to_dashboard'),
    path('add_collaborator/<int:project_id>/<str:username>/', views.add_collaborator, name='add_collaborator'),
    #path('remove_collaborator/<int:user_id>/', views.remove_collaborator, name='remove_collaborator'),
    path('set_deadline/<int:project_id>/<int:task_id>/<str:user_name>/', views.set_deadline, name='set_deadline'),
    path('notifications/<int:user_id>/', views.notifications, name='notifications'),
    path('complete_task/<int:task_id>/', views.complete_task, name='complete_task'),

]

