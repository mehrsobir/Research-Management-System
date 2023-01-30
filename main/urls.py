from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('plan/', views.plan, name='plan'),
    path('article/', views.article, name='article'),
]
