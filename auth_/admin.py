from django.contrib import admin
from .models import UserProfile, MainUser
# Register your models here.

admin.site.register(UserProfile)
admin.site.register(MainUser)