from django.urls import path, include
from rest_framework.routers import DefaultRouter

# We'll register our viewsets here
router = DefaultRouter()

app_name = "books"

urlpatterns = [path("", include(router.urls))]
