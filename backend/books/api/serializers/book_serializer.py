"""
Serializers for Book model.
Serializers convert complex data types (like Django models) to Python data types
that can be easily rendered into JSON for API responses.
"""

from rest_framework import serializers


class BookSerializer(serializers.ModelSerializer):
    """
    Serializer for Book model.
    """

    pass
