"""
Admin configuration for custom User model.
"""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    # Admin interface for custom User model.

    list_display = ["username", "email", "name", "is_active", "is_staff"]
    list_filter = ["is_active", "is_staff", "date_joined"]
    search_fields = ["email", "username", "name"]
    ordering = ["username"]

    fieldsets = BaseUserAdmin.fieldsets + (("Additional Info", {"fields": ("name",)}),)

    add_fieldsets = BaseUserAdmin.add_fieldsets + (
        (
            "Additional Info",
            {
                "fields": (
                    "email",
                    "name",
                )
            },
        ),
    )
