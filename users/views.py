from django.contrib import messages
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import Group, Permission
from .models import NewUser
from django.contrib.contenttypes.models import ContentType
from main.forms import RegisterForm

# from django.contrib.auth import get_user_model
# User = get_user_model()

def give_perm(request):
    ct = ContentType.objects.get_for_model(model=NewUser)
    perm = Permission.objects.filter(content_type = ct)

    user = NewUser.objects.get(email='m@m.tj')
    grup = Group.objects.get(name = 'management')
    grup.user_set.add(user)
    print(grup)
    return HttpResponse('df')


def user_register(request):
    context = {}
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
        else:
            context['registration_form'] = form
    else:
        form = RegisterForm()
        context['registration_form'] = form

    return render(request, 'users/register.html', context)

def user_login(request):
    if request.method == 'POST':
        username = request.POST['email']
        password = request.POST['password']
        user = authenticate(username = username, password = password)
        print(request.POST)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Логин ё парол хато аст. Лутфан, аз нав ворид шавед!!')
            return redirect('/login')

    return render(request, 'users/login.html') #HttpResponse('<h1>Саҳифаи login</h1>') #

def user_logout(request):
    # if request.method == 'POST':
    logout(request)
    return redirect('login')
    # return render(request, 'users/login.html')