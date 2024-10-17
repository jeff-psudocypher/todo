from django.http import HttpResponse
from django.shortcuts import  render
from todos.models import Task
def home(request):
    task=Task.objects.filter(is_completed=False).order_by('-modified_at')
    # task_done=Task.objects.filter(is_completed=True)
    print(task)
    return render(request,'home.html',{'task' : task})