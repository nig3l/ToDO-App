from django.shortcuts import render
from django.http import HttpResponse
import requests
from . models import *

# Create your views here.

def index(request):

    tasks = Task.objects.all()
    context = {'tasks':tasks}

    return render(request , 'chimztasks/list.html', context)
