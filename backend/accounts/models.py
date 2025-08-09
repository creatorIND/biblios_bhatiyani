"""
Custom User model for Biblios.
Requirements: email, password, name for user authentication.
"""

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Custom User model extending Django's AbstractUser."""

    # Override email to ensure it's unique and required
    email = models.EmailField(unique=True, max_length=255)

    # Add custom name field
    name = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.username

    def get_full_name(self):
        # Return the name of the user.
        if self.name:
            return self.name
        return super().get_full_name()

    def get_short_name(self):
        # Return the short name for the user.
        if self.name:
            return self.name.split()[0] if self.name else self.username
        return super().get_short_name()

    class Meta:
        db_table = "users"
        verbose_name = "User"
        verbose_name_plural = "Users"
