from django.contrib import admin
from App_Login.models import UserProfile
from django.contrib.auth.models import Group

# Register your models here.

admin.site.register(UserProfile)
admin.site.unregister(Group)