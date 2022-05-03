from django.shortcuts import render
import datetime

# Create your views here.
def index(request):
    now = datetime.datetime.now()
    return render(request, 'mybirthday/index.html', {
      "mybirthday": now.month == 8 and now.day == 20
    })