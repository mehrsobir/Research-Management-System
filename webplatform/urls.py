from django.contrib.auth.views import PasswordChangeView
from django.contrib import admin
from django.urls import path, include
from users import views as user_views
from users.views import change_password

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('login/', user_views.user_login, name='login'),
    path('logout/', user_views.user_logout, name='logout'),
    # path('register/', user_views.user_register, name='register'),
    path('changepassword/', change_password, name='change_password'),


]
