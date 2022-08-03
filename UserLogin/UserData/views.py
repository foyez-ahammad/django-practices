from django.shortcuts import render, HttpResponseRedirect
from .forms import UserForm
from .models import User

# Create your views here.

#Create -Add Data
def create(request):
    # if method "POST"
    if request.method == 'POST':
        form = UserForm(request.POST)

        # #first way save form data
        # if form.is_valid():
        #     form.save()
        #     # for return blank forms
        #     form = UserForm()

        # Second way save form data
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            # models user function call
            form_initialize = User(
                name=name, email=email, password=password)
            form_initialize.save()

            # for blank forms
            form = UserForm()


    # if method "GET"
    else:
        form = UserForm()
    return render(request, 'create.html', {'form': form})

#Read -view data
def read(request):
    userd = User.objects.all()
    return render(request, 'read.html', {'data': userd})

#Delete -Delete
def delete(request, id):
    if request.method =='POST':
        primary_id = User.objects.get(pk=id)
        primary_id.delete()
        return HttpResponseRedirect('http://127.0.0.1:8000/')

#Update -edit data
def update(request, id):
    if request.method =='POST':
        primary_id = User.objects.get(pk=id)
        form = UserForm(request.POST, instance=primary_id)
        if form.is_valid():
            form.save()
    else:
        primary_id = User.objects.get(pk=id)
        form = UserForm(instance=primary_id)
    return render(request, 'update.html', {'form':form})



