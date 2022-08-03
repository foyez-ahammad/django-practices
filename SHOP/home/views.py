from django.shortcuts import render
from django.contrib import messages
from .models import Contact


def home(request):
    return render(request, 'home/home.html')


def about(request):
    name = 'Foyez Ahammad'
    skill = ' Git & Github, Django, MySQL, Basic Front-End (HTML, CSS, JS, Bootstrap), Django REST Framework'
    skill_know = '1. Python 2. Git & Github 3. Django 4. MySQL 5. A little bit (HTML, CSS, Bootstrap). '
    gpa = 'GPA: 5.00'

    # For Template tag condition
    num = 10
    knowledge = {'knowledge': ['Python', 'Git & Github', 'Django', 'MySQL']}
    context = {'name': name, 'skill': skill,
               'skill_know': skill_know, 'gpa': gpa, 'num': num}

    return render(request, 'home/about.html', context=context)
    return render(request, 'home/about.html', context=knowledge)


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
        messages.success(request, 'Successfully, ')
    return render(request, 'home/contact.html')
