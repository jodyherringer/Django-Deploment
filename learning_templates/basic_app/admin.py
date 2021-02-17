from django.contrib import admin
from basic_app.models import User, UserAdmin

# Register your models here.
admin.site.register(User,UserAdmin)