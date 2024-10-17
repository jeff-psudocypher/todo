from django.shortcuts import render
from django.http import HttpResponse
from .models import Task
from django.shortcuts import redirect,get_object_or_404
# Create your views here.

def addtask(request):
    if(request.method=='POST'):
        task=request.POST.get('task')
        Task.objects.create(task=task)
        return redirect('home')
    return render(request,'home.html')
    # return HttpResponse('form is submitted')

def mark_as_done(request,i):
    task=get_object_or_404(Task,id=i)
    task.is_completed = True
    task.save()
    return redirect('home')

def mark_as_undone(request,i):
    task = get_object_or_404(Task, id=i)
    task.is_completed = False
    task.save()
    return redirect('home')

def edit_task(request,i):
    get_task = get_object_or_404(Task,id=i)
    if(request.method=='POST'):
        new_task=request.POST['task']
        get_task.task=new_task
        get_task.save()
        return redirect('home')
    return render(request,'edit.html',{'get_task':get_task})


def delete_task(request,i):
    task=get_object_or_404(Task,id=i)
    task.delete()
    return redirect('home')