"""
API views for Book operations.
Views handle the business logic and return API responses.
"""

from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response


class BookViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Book CRUD operations.
    Provides list, create, retrieve, update, and delete actions.
    """

    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """
        Return books for the current user only.
        Users should only see their own books.
        """
        pass
