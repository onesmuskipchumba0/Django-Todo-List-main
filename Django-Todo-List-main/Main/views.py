from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse,HttpResponseRedirect
from .models import Todo
# Create your views here.
def index(req):
    if req.method == 'POST':
        todo_title = req.POST['todo']
        if todo_title != '':
            new_todo = Todo(title = todo_title)
            new_todo.save()
            return render(req, 'index.html',{
                'todos':Todo.objects.all()
                })
        else:
            return render(req, 'index.html',{
                'todos':Todo.objects.all()
                })
    return render(req, 'index.html',{
        'todos':Todo.objects.all()
    })
    
def delete_todo(req, todo_id):
    todo_to_del = Todo.objects.get(pk=todo_id)
    todo_to_del.delete()
    return render(req, 'index.html',{
        'todos':Todo.objects.all()
    })

def update_todo(req, todo_id):
    if req.method == 'POST':
        todo_text = req.POST['todo_text']
        todo_to_update = Todo.objects.get(pk = todo_id)
        if todo_text != '':
            todo_to_update.title = todo_text
            todo_to_update.save()
        return HttpResponseRedirect(reverse("index"))
                
    return render(req, 'update.html',{
        'todo':Todo.objects.get(pk = todo_id)
    })