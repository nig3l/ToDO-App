from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def Taskview(request):
    return HttpResponse ('To Do List')

