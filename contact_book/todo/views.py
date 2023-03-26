from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.db.models import Q


from .forms import TodoForm
from .models import Todo


def index(req):
    # search = req.GET['search'].strip() if 'search' in req.GET.keys() else None
    search = req.GET.get('search', '').strip()
    if search:
        todos = Todo.objects.filter(
            Q(title__icontains=search) | Q(description__icontains=search))
    else:
        todos = Todo.objects.all()
    return render(req, 'todo/index.html', {'todos': todos})


def view(req, id):
    todo = Todo.objects.get(id=id)
    return render(req, 'todo/view.html', {'todo': todo})


def create(req):
    context = {
        'form': TodoForm()
    }
    if req.method == 'GET':
        return render(req, 'todo/create.html', context)
    elif req.method == 'POST':
        form = TodoForm(req.POST)
        if form.is_valid():
            form.save()
            context['form'] = form
            return redirect('todo.index')
        else:
            messages.add_message(req, messages.ERROR, 'Error')
            return render(req, 'todo/create.html', context)

    return HttpResponse('Not allowed')


def edit(req, id):
    try:
        todo = Todo.objects.get(id=id)
    except:
        todo = Todo()

    context = {
        'id': id,
    }
    if req.method == 'GET':
        context['form'] = TodoForm(instance=todo)
        return render(req, 'todo/create.html', context)
    elif req.method == 'POST':
        form = TodoForm(data=req.POST, instance=todo)
        if form.is_valid():
            form.save()
            context['form'] = form
            messages.add_message(req, messages.SUCCESS, 'Saved')
        else:
            messages.add_message(req, messages.ERROR, 'Error')
        return render(req, 'todo/create.html', context)

    return HttpResponse('Not allowed')


def delete(req, id):
    try:
        todo = Todo.objects.get(id=id)
    except:
        todo = Todo()

    if req.method == 'GET':
        todo.delete()
        return redirect('todo.index')

    return HttpResponse('Not allowed')
