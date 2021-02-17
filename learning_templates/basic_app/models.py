from django.db import models
from django.contrib import admin

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    email = models.EmailField(max_length=254,unique=True)

class UserAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name','email']

# Create your models here.
