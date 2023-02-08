from django.urls import path
from . import views

urlpatterns = [
    path('add/plan', views.add_plan, name='add-plan'),
    path('get/plan', views.get_plan, name='get-plan'),
    path('add/subtopic/<plan_id>', views.add_subtopic, name='add-subtopic'),
    path('update/subtopic/<sub_id>', views.update_subtopic, name='update-subtopic'),
    path('del/subtopic/<sub_id>', views.del_subtopic, name='del-subtopic'),


]