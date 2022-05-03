from django.shortcuts import render

tasks = ["Étudier Français", "Étudier l'anglais", "Étudier AWS", "Étudier Python" ]

# Create your views here.
def index(request):
    return render(request, 'tasks/index.html', {
      'tasks': tasks
    })

def add(request):
    # tasks.append(request.POST['task'])
    return render(request, 'tasks/add.html')