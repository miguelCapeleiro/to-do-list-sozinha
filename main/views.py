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

def task_create(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo', '').strip()
        descricao = request.POST.get('descricao', '').strip()
        concluida = request.POST.get('concluida', '') =='on'
        data_limite = request.POST.get('data_limite', '').strip()
        prioridade = request.POST.get('prioridade', '').strip()
    
    context = {
        'opcoes_prioridade': Task.Priority.choices,
    }

    return render(request, 'tasks/task_form.html', context)