from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import ugettext_lazy as _

from custom_auth.models import User
from custom_auth.forms import UserCreationForm, UserChangeForm


class UserAdmin(BaseUserAdmin):

    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('username', 'email', 'is_staff')
    list_filter = ('is_staff',)
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        (_('Permissions'),
            {'fields': ('is_staff', 'groups', 'user_permissions')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'date_joined',
                       'password1', 'password2'),
        }),
    )
    search_fields = ('username', 'email',)
    ordering = ('username', 'email',)
    filter_horizontal = ()


admin.site.register(User, UserAdmin)
