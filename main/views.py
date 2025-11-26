from django.shortcuts import render
from .models import Task
# Create your views here.

def task_list(request):
    
    tarefas = Task.objects.all()
    context = {
        'tarefas':tarefas
    }

    return render(request, 'tasks/task_list.html', context)

def tasks_ok(request):
    
    tarefas = Task.objects.filter(concluida=1)
    context = {
        'tarefas':tarefas
    }

    return render(request, 'tasks/task_list.html', context)

def tasks_nok(request):
    tarefas = Task.objects.filter(concluida=0)
    context = {
        'tarefas':tarefas
    }

    return render(request, 'tasks/task_list.html', context)

def home(request):
    
    tarefas = Task.objects.all()
    context = {
        'tarefas':tarefas
    }

    return render(request, 'home.html', context)
