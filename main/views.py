from django.shortcuts import render, redirect, get_object_or_404
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
        
        Task.objects.create(
            titulo=titulo,
            descricao=descricao,
            concluida=concluida,
            prioridade=prioridade,
            data_limite=data_limite
        ) 
        
        return redirect ('task_list')
    
    
    context = {
        'opcoes_prioridade': Task.Priority.choices,
    }

    return render(request, 'tasks/task_form.html', context)



def task_update(request, pk):
    task = get_object_or_404(Task, pk = pk)
    if request.method == 'POST':
        titulo = request.POST.get('titulo', '').strip()
        descricao = request.POST.get('descricao', '').strip()
        concluida = request.POST.get('concluida', '') =='on'
        data_limite = request.POST.get('data_limite', '').strip()
        prioridade = request.POST.get('prioridade', '').strip()
        
        
        task.titulo=titulo
        task.descricao=descricao
        task.concluida=concluida
        task.prioridade=prioridade
        task.data_limite=data_limite
        task.save()
        
        return redirect ('task_list')
    
    
    context = {
        'opcoes_prioridade': Task.Priority.choices,
        'task': task,
    }

    return render(request, 'tasks/task_form.html', context)



def task_delete (request, pk):
    task = get_object_or_404(Task,pk=pk)
    
    if request.method == 'POST':
        task.delete()
        return redirect(task_list)
    return render(request, 'tasks/task_confirm_delete.html')