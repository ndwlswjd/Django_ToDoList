from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import *

def index(request):
    todos = Todo.objects.all()
    content = {'todos' : todos}
    return render(request, 'my_to_do_app/index.html', content)

def createTodo(request):
    user_input_str = request.POST['todoContent']
    new_todo = Todo(content = user_input_str)
    new_todo.save()
    return HttpResponseRedirect(reverse('index'))
    #return HttpResponse("create Todo=> "+user_input_str)

def deleteTodo(request):
    user_delete_todoNum = request.GET['todoNum']
    delete_todo = Todo(id = user_delete_todoNum)
    delete_todo.delete()
    return HttpResponseRedirect(reverse('index'))
