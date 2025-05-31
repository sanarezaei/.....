from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User
from .forms import CustomUserChangeForm, CustomUserCreationForm

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    filter_horizontal = ()

    list_display = ('phone_number', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active' ,'is_active')

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