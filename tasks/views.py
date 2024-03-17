from django.shortcuts import render, redirect
from .models import Project, Task
from django.contrib.auth.decorators import login_required
from django.http import Http404
from .forms import TimerForm

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
def delete_task(request, task_id):
    task = Task.objects.get(pk=task_id)    #pk=primary key
    if request.method == 'POST':
        task.delete()
    return redirect('project_page', project_id=task.parent_project_id)


def task_page(request):
    # Retrieve tasks from the database or create a queryset as needed
    tasks = Task.objects.all()
    form = TimerForm()
    return render(request, 'task_page.html', {'tasks': tasks})

    context = {
        'tasks': tasks,
        'form': form,
    }
    return render(request, 'timer.html', context)


def start_timer(request, task_id):
    task = Task.objects.get(id=task_id)
    # Start the timer logic here
    return redirect('task_page.html')

def stop_timer(request, task_id):
    task = Task.objects.get(id=task_id)
    # Stop the timer logic here
    return redirect('task_page.html')

def reset_timer(request, task_id):
    task = Task.objects.get(id=task_id)
    # Reset the timer logic here
    return redirect('task_page.html')

def pause_timer(request, task_id):
    task = Task.objects.get(id=task_id)
    # Pause the timer logic here
    return redirect('task_page.html')



