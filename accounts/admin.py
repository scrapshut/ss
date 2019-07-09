from django.contrib import admin
from .models import User
# from .forms import
from django.contrib.auth.admin import UserAdmin

from .forms import UserRegistrationForm
# Register your models here.
# admin.site.register(User)
class CustomUserAdmin(UserAdmin):
    model = User
    form = UserRegistrationForm
    # form = CustomUserChangeForm

admin.site.register(User, CustomUserAdmin)
