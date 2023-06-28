from django import forms
from django.forms import ModelForm

from .models import *

class TaskForm(forms.ModelForm):

    task = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'add new task ....'}))

    class Meta:
        model = Task
        fields = '__all__'
        
