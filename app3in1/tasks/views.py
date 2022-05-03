from django import forms
from django.shortcuts import render

tasks = ["Étudier Français", "Étudier l'anglais", "Étudier AWS", "Étudier Python" ]

class NewTaskForm(forms.Form):
    task = forms.CharField(label='Nouvelle tâche')
    priority = forms.IntegerField(label='Priorité', min_value=1, max_value=5)

# Create your views here.
def index(request):
    return render(request, 'tasks/index.html', {
      'tasks': tasks
    })

def add(request):
    # tasks.append(request.POST['task'])
    return render(request, 'tasks/add.html',{
      'form': NewTaskForm()
    })