from django.contrib.auth.views import PasswordChangeView
from django.contrib import admin
from django.urls import path, include
from users import views as user_views
from users.views import change_password, update_user_info
from institutions.views import institute, department

urlpatterns = [
    path('admin/', admin.site.urls),
    # Main Page
    path('', include('main.urls')),
    path('login/', user_views.user_login, name='login'),
    path('logout/', user_views.user_logout, name='logout'),
    path('changepassword/', change_password, name='change-password'),
    path('update_user_info/', update_user_info, name='update-user-info'),
    #  Institution
    path('institute/', institute, name='institute'),
    #  Department
    path('department/', department, name='department'),

]
