from django.shortcuts import render, redirect, get_object_or_404
from .models import Project, Task
from django.contrib.auth.decorators import login_required
from django.http import Http404
from .forms import TimerForm
from django.contrib.auth.models import User
from django.contrib import messages
@login_required
def create_project(request):
    if request.method == 'POST':
        project_name = request.POST.get('project_name')
        if project_name:
            project = Project.objects.create(project_name=project_name, created_by=request.user)
            return redirect('dashboard')  
    return render(request, 'authentication/dashboard.html')

@login_required
def project_page(request, project_id):
    try:
        project = Project.objects.get(pk=project_id)
        project_tasks = Task.objects.filter(parent_project_id=project_id)
    except Project.DoesNotExist:
        raise Http404("Project does not exist")

    return render(request, 'project_page.html', {'project': project, 'project_tasks': project_tasks})

@login_required
def create_task(request, project_id):
    project = Project.objects.get(pk=project_id)

    if request.method == 'POST':
        task_name = request.POST.get('task_name')
        if task_name:
            task = Task.objects.create(task_name=task_name, parent_project=project)
            return redirect('project_page', project_id=project_id)
    
    return render(request, 'create_task.html', {'project': project})

@login_required
def delete_project(request, project_id):
    try:
        project = Project.objects.get(pk=project_id)
    except Project.DoesNotExist:
        raise Http404("Project does not exist")

    if request.method == 'POST':
        project.delete()
    return redirect('dashboard')

@login_required
def delete_task(request, task_id):
    task = Task.objects.get(pk=task_id)
    if request.method == 'POST':
        task.delete()
    return redirect('project_page', project_id=task.parent_project_id)

@login_required
def task_page(request):
    tasks = Task.objects.all()
    form = TimerForm()
    context = {'tasks': tasks, 'form': form}
    return render(request, 'task_page.html', context)

@login_required
def start_timer(request, task_id):
    # Start timer logic
    return redirect('task_page')

@login_required
def stop_timer(request, task_id):
    # Stop timer logic
    return redirect('task_page')

@login_required
def reset_timer(request, task_id):
    # Reset timer logic
    return redirect('task_page')

@login_required
def pause_timer(request, task_id):
    # Pause timer logic
    return redirect('task_page')

@login_required
def back_to_dashboard(request):
    return redirect('dashboard')

@login_required
def dashboard(request):
    fname = request.user.first_name
    user_projects = Project.objects.filter(created_by=request.user)
    return render(request, 'authentication/dashboard.html', {'user_projects': user_projects,'fname': fname})

@login_required
def add_collaborator(request, project_id, username):
    project = get_object_or_404(Project, project_id=project_id)
    collaborator = get_object_or_404(User, username=username)
    project.collaborators.add(collaborator)

    messages.success(request, f"{collaborator.username} added as a collaborator to the project.")
    return redirect('project_page', project_id=project_id)

@login_required
def remove_collaborator(request, project_id, username):
    project = get_object_or_404(Project, id=project_id)
    collaborator = get_object_or_404(User, username=username)
    project.collaborators.remove(collaborator)
    return redirect('dashboard')
