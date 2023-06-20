from django.urls import path
from . import views

urlpatterns =[
    path('',views.Taskview,name='tasks')
]