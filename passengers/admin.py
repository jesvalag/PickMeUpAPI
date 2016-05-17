from .models import Passenger
from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from import_export.admin import ImportExportMixin

class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField(label=("Password"),
                                         help_text=("Raw passwords are not stored, so there is no way to see "
                                                    "this user's password, but you can change the password using "
                                                    "<a href=\'../password/\'>this form</a>."))

    class Meta:
        model = Passenger
        fields = ('email',)

    def clean_password(self):
        return self.initial['password']


class PassengerAdmin(ImportExportMixin, BaseUserAdmin):
    form = UserChangeForm
    list_display = ("username", "first_name", "last_name", "email",)
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password', 'reset_password_code')}),
        ('Personal info', {'fields': ('first_name',
                                      'last_name',
                                      'skype_id',)}),
        ('Permissions', {'fields': ('groups',
                                    'user_permissions',
                                    'is_superuser',
                                    'is_staff',
                                    'is_active',)}),
        ('History', {'fields': ('date_joined', 'last_login')})
    )

admin.site.register(Passenger, PassengerAdmin)

