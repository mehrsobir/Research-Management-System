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

def group_add_user(request):
    # ct = ContentType.objects.get_for_model(model=NewUser)
    # perm = Permission.objects.filter(content_type = ct)
    # grup.user_set.remove(user)

    user = NewUser.objects.get(id=1)
    group_name = request.GET.get('group','')
    group = Group.objects.get(name=group_name)
    group.user_set.add(user)
    messages.info(request, f'{user.first_name} added to group {group}!!')
    return redirect('/')

def group_remove_user(request):
    user = NewUser.objects.get(id=1)
    group_name = request.GET.get('group','')
    group = Group.objects.get(name=group_name)
    group.user_set.remove(user)
    messages.info(request, f'{user.first_name} removed from group {group}!!')
    return redirect('/')


def user_register(request):
    context = {}
    if request.method == 'POST':
        form = RegisterForm(request.POST)
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

    return render(request, 'users/login.html')

def user_logout(request):
    logout(request)
    return redirect('login')