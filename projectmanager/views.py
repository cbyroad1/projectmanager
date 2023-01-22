from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Project, Task
from .forms import MyUserCreationForm, Projectform, LoginForm, Taskform
from django.contrib.auth import authenticate, login, logout
import datetime
from django.contrib import messages


def home(request):
    user = request.user
    projects = ''
    tasks = ''
    overall_projects = ''
    completed_tasks = ''

    if request.user.is_authenticated:
        username = (request.user)
        tasks = Task.objects.filter(creator=username).order_by('due_date')
        completed_tasks = Task.objects.filter(creator=username).order_by('-date_completed')
        projects = Task.objects.values_list('project__project_title', flat=True).distinct()
        overall_projects = Project.objects.filter(creator=username)
    
    print(projects)
       
    context = {'projects':projects, 'user':user, 'tasks':tasks, 'overall_projects':overall_projects, 'completed_tasks':completed_tasks}
    return render(request, 'home.html', context)

def add_project(request):

    if request.method == "POST":
        form = Projectform(request.POST)
        if form.is_valid():
            form.instance.creator = request.user
            form.save()
            return redirect('/')
    else:
        form = Projectform()

    context = {'form':form}
    return render(request, 'add_project.html', context)



def registerUser(request):
    page = ''
    if request.method == "POST":
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('loginUser')
        else:
            return HttpResponse('Your Passwords Did Not Match')
    else:
        form = MyUserCreationForm
    
    context = {'form':form, 'page':page}
    return render(request, 'register.html', context)



def loginUser(request):
    page = 'login'
    
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                messages.add_message(request, messages.ERROR, "The username and password combination was incorrect")
        else:
            return HttpResponse('There was an error processing your request')
    else:
        form = LoginForm
    
    context = {'page':page, 'form': form}
    return render(request, 'register.html', context)




def logoutUser(request):
    logout(request)
    return redirect('home')



def deleteProject(request, pk):
    project = Project.objects.get(id=pk)
    page = 'deleteProject'

    if request.method == "POST":
        project.delete()
        return redirect('home')

    context = {'project':project, 'page':page}
    return render(request, 'delete.html', context)



def completeProject(request, pk):
    project = Project.objects.get(id=pk)
    page = 'completeProject'

    if request.method == "POST":
        project.set_complete()
        return redirect('home')

    context = {'project':project, 'page':page}
    return render(request, 'completed.html', context)



def add_task(request):

    if request.method == "POST":
        form = Taskform(request.POST)
        if form.is_valid():
            form.instance.creator = request.user
            form.save()
            return redirect('/')
    else:
        form = Taskform()

    context = {'form':form}
    return render(request, 'add_task.html', context)

def completeTask(request, pk):
    task = Task.objects.get(id=pk)
    page = 'completeTask'

    if request.method == "POST":
        task.set_complete()
        return redirect('home')

    context = {'task':task, 'page':page}
    return render(request, 'completed.html', context)

def deleteTask(request, pk):
    task = Task.objects.get(id=pk)
    page = 'deleteTask'

    if request.method == "POST":
        task.delete()
        return redirect('home')

    context = {'task':task, 'page':page}
    return render(request, 'delete.html', context)