from django.contrib import admin
from .models import Route


class RouteAdmin(admin.ModelAdmin):
    list_display = ("departure", "arrival", )

admin.site.register(Route, RouteAdmin)