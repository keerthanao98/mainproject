from django.contrib import messages
from django.shortcuts import render, redirect

# Create your views here.
from collegeapp.forms import ProfileForm
from collegeapp.models import Todo


def home(request):
    return render(request,'modified_files/home.html')


def profile(request):
    return render(request,'index.html')

def create(request):
    form = ProfileForm()
    if request.method =='POST':
        form = ProfileForm(request.POST)
        form.save()
        messages.info(request, 'Account created successfully')
        return redirect('view')
    return render(request,'form.html',{"form":form})

def view(request):
    data = Todo.objects.all()

    return render(request,'view.html',{"data":data})

def update(request,Todo_id):
    todo = Todo.objects.get(id=Todo_id)
    form = ProfileForm(instance=todo)
    if request.method == 'POST':
        form = ProfileForm(request.POST,instance=todo)
        if form.is_valid():
            form.save()
        messages.info(request,'updated successfully')
        return redirect('view')
    return render(request,'update.html',{"form":form})


def delete(request,Todo_id):
    todo = Todo.objects.get(id=Todo_id)
    todo.delete()
    return redirect('view')


