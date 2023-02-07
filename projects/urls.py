from django.urls import path
from . import views

urlpatterns = [
    path('add/plan', views.add_plan, name='add-plan'),
    path('get/plan', views.get_plan, name='get-plan'),
    path('add/subtopic/<plan_id>', views.add_subtopic, name='add-subtopic'),
    # path('get/subtopic', views.get_subtopic, name='get-subtopic'),


]