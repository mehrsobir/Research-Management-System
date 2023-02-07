from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required, permission_required
from .forms import PlanForm, SubtopicForm
from .models import Plan, Topic, Project, Subtopic
from institutions.models import User_job, Job
from django.db import IntegrityError


@login_required(login_url="login")
def add_plan(request):
    dep_id = User_job.objects.filter(user=request.user).filter(disabled = False).select_related('job').get().job.department.id
    if request.method == 'POST':
        form = PlanForm(request.POST)
        form.fields["topic"].queryset = Topic.objects.filter(project=dep_id)
        try:
            if form.is_valid():
                plan = form.save(commit=False)
                plan.user = request.user
                plan.save()
                return render(request,'partials/success.html')
        except IntegrityError as e:
            error = 'Дар як сол як нақшаи инфродӣ бояд бошад!!!'
    else:
        form = PlanForm()
        error = ''
        form.fields["topic"].queryset = Topic.objects.filter(project = dep_id)
    return render(request, 'partials/add_plan.html', { 'form': form, 'error': error} )

@login_required(login_url="login")
def get_plan(request):
    plan = Plan.objects.filter(user=request.user).filter(year=2023).get()
    subtopic = Subtopic.objects.filter(plan_id=plan)
    return render(request, 'partials/get_plan.html', { 'plan': plan, 'subtopic': subtopic} )

@login_required(login_url="login")
def add_subtopic(request, plan_id):
    if request.method == 'POST':
        form = SubtopicForm(request.POST)
        if form.is_valid():
            plan = form.save(commit=False)
            plan.plan_id = Plan.objects.get(id=plan_id)
            plan.save()
            return render(request,'partials/success.html')

    else:
        form = SubtopicForm()
        error = ''
        # form.fields["topic"].queryset = Topic.objects.filter(project = dep_id)
    return render(request, 'partials/add_subtopic.html', { 'form': form, 'error': error} )



