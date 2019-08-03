# from django.contrib import admin
# # from .models import User
# # from .forms import
# from django.contrib.auth.admin import UserAdmin
# from .forms import UserRegistrationForm
# # Register your models here.
# # admin.site.register(User)
# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# from .models import User, UserProfile
#
#
# class UserProfileInline(admin.StackedInline):
#     model = UserProfile
#     can_delete = False
#     verbose_name_plural = 'profile'
#
#
# class UserAdmin(admin.ModelAdmin):
#     inlines = (UserProfileInline, )
# class CustomUserAdmin(UserAdmin):
#     model = User
#     form = UserRegistrationForm
#
# admin.site.register(User, UserAdmin)
#
#     # form = CustomUserChangeForm
#
# admin.site.register(User, CustomUserAdmin)
# admin.site.register(Connection)


from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, UserProfile


class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'profile'


class UserAdmin(admin.ModelAdmin):
    inlines = (UserProfileInline, )

admin.site.register(User, UserAdmin)
