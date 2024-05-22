from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('name', 'email', 'number')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('name', 'email', 'number')}),
    )
    list_display = ('username', 'name', 'email', 'number', 'is_staff', 'is_active')
    search_fields = ('username', 'name', 'email', 'number')

admin.site.register(CustomUser, CustomUserAdmin)