from django.urls import path
from .views import TaskList , TaskDetail

urlpatterns =[
    path('',TaskList.as_view(),name='tasks'),
    path('',TaskDetail.as_view(),name='task detail')
]