from django.contrib import admin
from .models import  Nationality, Education, Direction, Category, Status

admin.site.register(Nationality)
admin.site.register(Education)
admin.site.register(Direction)
admin.site.register(Category)
admin.site.register(Status)