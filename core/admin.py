from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User

class CustomUserAdmin(UserAdmin):
    list_display = ('phone_number', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active' ,'is_active')
    filter_horizontal = ()

    fieldsets = (
        (None, {'fields': ('phone_number', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'phone_number',
                'password',
                'password2',
                'is_staff',
                'is_active'
            ),
        }),
    )

    search_fields = ('phone_number',)
    ordering = ('phone_number', )

admin.site.register(User, CustomUserAdmin)