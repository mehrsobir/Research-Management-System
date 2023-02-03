from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required, permission_required
from .forms import PlanForm
from .models import Plan


@login_required(login_url="login")
def add_plan(request):
    if request.method == 'POST':
        form = PlanForm(request.POST)
        if form.is_valid():
            plan = form.save(commit=False)
            plan.user = request.user
            plan.save()
            return render(request,'partials/success.html')
    else:
        form = PlanForm()
    return render(request, 'partials/add_plan.html', { 'form': form,} )

