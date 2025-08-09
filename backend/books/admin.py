"""
Admin configuration for Book model.
"""

from django.contrib import admin
from .models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # Admin interface for Book model.
    list_display = [
        "title",
        "author",
        "status",
        "user",
        "get_progress",
        "created_at",
    ]
    list_filter = ["status", "genre", "created_at"]
    search_fields = ["title", "author", "user__email"]
    readonly_fields = [
        "created_at",
        "updated_at",
    ]

    fieldsets = (
        (
            "Book Information",
            {"fields": ("title", "author", "pages", "genre", "summary", "cover_image")},
        ),
        (
            "Reading Progress",
            {
                "fields": (
                    "status",
                    "current_page",
                ),
                "description": "Current page will be set to 0 by default for new books.",
            },
        ),
        ("Assignment", {"fields": ("user",)}),
        (
            "Timestamps",
            {"fields": ("created_at", "updated_at"), "classes": ("collapse",)},
        ),
    )

    def get_progress(self, obj):
        # Display progress percentage in list view.
        return f"{obj.progress_percentage}%"

    get_progress.short_description = "Progress"
