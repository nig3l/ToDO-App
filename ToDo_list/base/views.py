from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView

from .models import Task

# Create your views here.

class TaskList(ListView):
    model = Task
    context_object_name = 'task'

class TaskDetail(DetailView):
    model = Task
    context_object_name = 'task'
    
class TaskCreate(CreateView):
    model = Task
    field = '__all__'


