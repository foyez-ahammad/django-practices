from django.shortcuts import render, HttpResponseRedirect
from .models import Dept, Role, Employee
from datetime import datetime
from django.db.models import Q


def views(request):
    employee = Employee.objects.all()
    return render(request, 'views.html', {'employee': employee})


def adding(request):
    if request.method == 'POST':
        f_name = request.POST['f_name']
        l_name = request.POST['l_name']
        dept = request.POST['dept']
        salary = request.POST['salary']
        bonus = request.POST['bonus']
        role = request.POST['role']
        phone = request.POST['phone']

        employee = Employee(f_name=f_name, l_name=l_name, dept_id=dept, salary=salary,
                            bonus=bonus, phone=phone, role_id=role, hire_date=datetime.now())
        employee.save()

    return render(request, 'adding.html')



def delete(request, id):
    if request.method =='POST':
        primary_id = Employee.objects.get(pk=id)
        primary_id.delete()
        return HttpResponseRedirect('http://127.0.0.1:8000/')


def search(request):
    if request.method == 'POST':
        name = request.POST['name']
        dept = request.POST['dept']
        role = request.POST['role']
        phone = request.POST['phone']

        emp = Employee.objects.all()

        if name:
            emp = emp.filter(Q(f_name__icontains=name) |
                             Q(l_name__icontainer=name))
        if dept:
            emp = emp.filter(Q(dept__name__icontains=dept))
        if role:
            emp = emp.filter(Q(role__name__icontains=role))
        if phone:
            emp = emp.filter(Q(phone__icontains=phone))

        context = {
            'emp': emp
        }

        return render(request, 'views.html', context)

    return render(request, 'search.html')

def update(request, id):
    if request.method =='POST':
        primary_id = Employee.objects.get(pk=id)
        form = Employee(request.POST, instance=primary_id)
        if form.is_valid():
            form.save()
    else:
        primary_id = Employee.objects.get(pk=id)
        form = Employee(instance=primary_id)
    return render(request, 'update.html', {'form':form})
