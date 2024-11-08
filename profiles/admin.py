from django.contrib import admin
from .models import Profile, LoginHistory, CustomUser

# Register your models here.

admin.site.register(Profile)

admin.site.register(LoginHistory)
admin.site.register(CustomUser)
