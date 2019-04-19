
from django.shortcuts import render,redirect
from django.http import HttpResponse

from .models import Todo

def index(request):
    todos=Todo.objects.all()[:50]
    context={
    'todos':todos
    }
    return render(request,'index.html',context)

def details(request,id):
    todo = Todo.objects.get(id=id)

    context={
    'todos':todo
    }
    return render(request,'details.html',context)
def add(request):
    if(request.method == 'POST'):
        print request.POST
        title = request.POST['title']
        text =request.POST['text']
        email = request.POST['email']
        city = request.POST['city']
        date = request.POST['date']
        todo = Todo(title=title, text=text, email=email,city=city, date=date)
        todo.save()

        return redirect('/todos')

    else:
        return render(request,'partials/add.html')

def edit(request,id):
    print("id",id)
    todos=Todo.objects.get(pk=int(id))
    print todos
    context={
    'todos':todos,
    'title':todos.title,
    'text':todos.text,
    'email':todos.email,
    'city':todos.city,
    'date':todos.date
    }

    if(request.method == 'POST'):
        print request.POST
        todos.title = request.POST['title']
        todos.text =request.POST['text']
        todos.email =request.POST['email']
        todos.city = request.POST['city']
        todos.date = request.POST['date']
        todos.save()

        return redirect('/todos')


    return render(request,'partials/edit.html',context)

def delete(request,id):
    print("id",id)
    todos = Todo.objects.get(pk=id).delete()
    # print todos
    # # context={
    # 'todos':todos,
    # 'title':todos.title,
    # 'text':todos.text,
    # 'email':todos.email,
    # 'city':todos.city,
    # 'date':todos.date
    # }
    # if(request.method == 'POST'):
    #     print request.POST
    #     todos.title = request.POST['title']
    #     todos.text =request.POST['text']
    #     todos.email =request.POST['email']
    #     todos.city = request.POST['city']
    #     todos.date = request.POST['date']
    #     todos.save()

    return redirect('/todos')
