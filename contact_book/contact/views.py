from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages


from .forms import ContactForm
from .models import Contact


def index(req):
    # search = req.GET['search'].strip() if 'search' in req.GET.keys() else None
    search = req.GET.get('search', '').strip()
    if search:
        contacts = Contact.objects.filter(name__icontains=search)
    else:
        contacts = Contact.objects.all()
    return render(req, 'contact/index.html', {'contacts': contacts})


def view(req, id):
    contact = Contact.objects.get(id=id)
    return render(req, 'contact/view.html', {'contact': contact})


def create(req):
    context = {
        'form': ContactForm()
    }
    if req.method == 'GET':
        return render(req, 'contact/create.html', context)
    elif req.method == 'POST':
        form = ContactForm(req.POST)
        if form.is_valid():
            form.save()
            context['form'] = form
            return redirect('contact.index')
        else:
            messages.add_message(req, messages.ERROR, 'Error')
            return render(req, 'contact/create.html', context)

    return HttpResponse('Not allowed')


def edit(req, id):
    try:
        contact = Contact.objects.get(id=id)
    except:
        contact = Contact()

    context = {
        'id': id,
    }
    if req.method == 'GET':
        context['form'] = ContactForm(instance=contact)
        return render(req, 'contact/create.html', context)
    elif req.method == 'POST':
        form = ContactForm(data=req.POST, instance=contact)
        if form.is_valid():
            form.save()
            context['form'] = form
            messages.add_message(req, messages.SUCCESS, 'Saved')
        else:
            messages.add_message(req, messages.ERROR, 'Error')
        return render(req, 'contact/create.html', context)

    return HttpResponse('Not allowed')


def delete(req, id):
    try:
        contact = Contact.objects.get(id=id)
    except:
        contact = Contact()

    if req.method == 'GET':
        contact.delete()
        return redirect('contact.index')

    return HttpResponse('Not allowed')
