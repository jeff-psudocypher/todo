from django.shortcuts import render
from django.http import HttpResponse
from .models import Task
from django.shortcuts import redirect
# Create your views here.

def addtask(request):
    if(request.method=='POST'):
        task=request.POST.get('task')
        Task.objects.create(task=task)
        return redirect('home')
    return render(request,'home.html')
    # return HttpResponse('form is submitted')