from django.shortcuts import render, redirect
from .models import Members
from .forms import MembersForm

from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse


def index(request):
    mymembers = Members.objects.all().values()
    template = loader.get_template('index.html')
    context = {
        'mymembers': mymembers
    }
    return render(request, 'index.html', context)


def add(request):
    if request.method == 'POST':
        form = MembersForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('index')
    else:
        form = MembersForm()
    context = {'form': form}
    return render(request, 'add.html', context)


def delete(request, id):
    member = Members.objects.get(id=id)
    member.delete()
    return redirect('index')


def update(request, id):
    primary_id = Members.objects.get(pk=id)
    if request.method == 'POST':
        form = MembersForm(request.POST, instance=primary_id)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        primary_id = Members.objects.get(pk=id)
        form = MembersForm(instance=primary_id)
    context = {
        'form': form,
    }
    return render(request, 'update.html', context)
