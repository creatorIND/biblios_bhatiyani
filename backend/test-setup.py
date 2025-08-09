#!/usr/bin/env python
"""Test if Django environment is set up correctly."""

import sys
import os

print(f"Python executable: {sys.executable}")
print(f"Python version: {sys.version}")
print(f"Current directory: {os.getcwd()}")

try:
    import django

    print(f"✅ Django {django.get_version()} is installed")
except ImportError:
    print("❌ Django is NOT installed")

try:
    import rest_framework

    print("✅ Django REST Framework is installed")
except ImportError:
    print("❌ Django REST Framework is NOT installed")

try:
    import corsheaders

    print("✅ django-cors-headers is installed")
except ImportError:
    print("❌ django-cors-headers is NOT installed")

# Check if we're using the right venv
if "venv" in sys.executable:
    print("✅ Using virtual environment")
else:
    print("⚠️  Not using virtual environment")
