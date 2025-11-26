from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('concluidas', views.tasks_ok, name= 'tasks_ok'),
    path('pendentes', views.tasks_nok, name = 'tasks_nok'),
    path('home', views.home, name = 'home'),
]

    
