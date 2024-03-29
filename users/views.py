from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.contrib.auth.models import Group, Permission
from .models import Account, Profile
from django.contrib.contenttypes.models import ContentType
from .forms import PassChangeForm, UserUpdateForm, ProfileUpdateForm

# from django.contrib.auth import get_user_model
# User = get_user_model()

# def group_add_user(request):
    # ct = ContentType.objects.get_for_model(model=NewUser)
    # perm = Permission.objects.filter(content_type = ct)
    # grup.user_set.remove(user)

# gr = Group.objects.get(name = 'institute')
# user.groups.add(gr)
# if user.groups.filter(name = 'institute').exists():
#     request.session['inst_role'] = True
# if user.groups.filter(name = 'department').exists():
#     request.session['dep_role'] = True

#     user = Account.objects.get(id=1)
#     group_name = request.GET.get('group','')
#     group = Group.objects.get(name=group_name)
#     group.user_set.add(user)
#     messages.info(request, f'{user.first_name} added to group {group}!!')
#     return redirect('/')
#
# def group_remove_user(request):
#     user = Account.objects.get(id=1)
#     group_name = request.GET.get('group','')
#     group = Group.objects.get(name=group_name)
#     group.user_set.remove(user)
#     messages.info(request, f'{user.first_name} removed from group {group}!!')
#     return redirect('/')


# def user_register(request):
#     context = {}
#     if request.method == 'POST':
#         form = RegisterForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect('/')
#         else:
#             context['registration_form'] = form
#     else:
#         form = RegisterForm()
#         context['registration_form'] = form
#
#     return render(request, 'users/register.html', context)

def user_login(request):
    if request.method == 'POST':
        username = request.POST['email']
        password = request.POST['password']
        user = authenticate(username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Логин ё парол хато аст. Лутфан, аз нав ворид шавед!!')
            return redirect('/login')

    return render(request, 'users/login.html')

@login_required(login_url="login")
def user_logout(request):
    logout(request)
    return redirect('login')

@login_required(login_url="login")
def change_password(request):
    if request.method == 'POST':
        form = PassChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            return render(request,'partials/success.html')
    else:
        form = PassChangeForm(request.user)
    return render(request, 'users/changepass.html', { 'form': form,} )

@login_required(login_url="login")
def update_user_info(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return render(request, 'main/home.html')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'u_form': u_form,
        'p_form': p_form

    }
    return render(request, 'users/profile.html', context)