from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required, permission_required

@login_required(login_url="login")
def home(request):
    return render(request, 'main/home.html')