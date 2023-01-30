from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required

@login_required(login_url="login")
def institute(request):
    # current_user_groups = request.user.groups.values_list("name", flat=True)
    context = {
        "not_main": True,
        "is_institute": True
    }
    return render(request, 'main/institute.html', context)

@login_required(login_url="login")
def department(request):
    department = request.user.department
    # print(department)
    context = {
        "not_main": True,
        "department": department
    }
    return render(request, 'main/department.html', context)