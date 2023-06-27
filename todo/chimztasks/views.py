from django.shortcuts import render, redirect
from django.http import HttpResponse
import requests


from . models import *
from .forms import *

# Create your views here.

def index(request):

    tasks = Task.objects.all()
    form = TaskForm()

    context = {'tasks':tasks , 'form':form}

    if request.method == 'POST' :
        form = TaskForm(request.POST)
        if form.is_valid():
          form.save()

          return redirect('/')



    return render(request , 'chimztasks/list.html', context)
