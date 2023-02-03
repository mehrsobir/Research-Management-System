from django.urls import path
from . import views

urlpatterns = [
    path('add/plan', views.add_plan, name='add-plan'),
    # path('logout', views.user_logout, name='logout'),
    # path('register', views.register, name='register'),


]