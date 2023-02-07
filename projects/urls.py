from django.urls import path
from . import views

urlpatterns = [
    path('add/plan', views.add_plan, name='add-plan'),
    path('get/plan', views.get_plan, name='get-plan'),
    # path('register', views.register, name='register'),


]