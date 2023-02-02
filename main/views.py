from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required, permission_required

@login_required(login_url="login")
def home(request):
    current_user_groups = request.user.groups.values_list("name", flat=True)
    context = {
        "is_institute": "institute" in current_user_groups,
        "is_department": "department" in current_user_groups,
    }
    return render(request, 'main/home.html', context)

@login_required(login_url="login")
def plan(request):
    return render(request, 'partials/plan.html')

@login_required(login_url="login")
def article(request):
    return render(request, 'partials/article.html')

@login_required(login_url="login")
def article_pub(request):
    return render(request, 'partials/article_pub.html')