from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser,Staff

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'role', 'is_staff', 'is_active')  # Display these fields in the admin panel
    list_filter = ('role', 'is_staff', 'is_active')  # Filters in the admin panel
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Role & Permissions', {'fields': ('role', 'is_staff', 'is_active', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'role', 'password1', 'password2'),
        }),
    )
    search_fields = ('username', 'email')
    
# Register CustomUser with the custom admin class
admin.site.register(CustomUser, CustomUserAdmin)
@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display=('gender','address','position','dob','salary','qualification')
    