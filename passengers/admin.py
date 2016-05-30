from .models import Passenger
from django.contrib import admin

class PassengerAdmin(admin.ModelAdmin):
    list_display = ("username", "first_name", "last_name", "email", )
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Personal info', {'fields': ('first_name',
                                      'last_name',
                                      'cellphone',
                                      'skype_id',)}),
        ('Permissions', {'fields': ('groups',
                                    'user_permissions',
                                    'is_superuser',
                                    'is_staff',
                                    'is_active',)}),
        ('History', {'fields': ('date_joined', 'last_login')})
    )

admin.site.register(Passenger, PassengerAdmin)

