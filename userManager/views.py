"""
Views for user API.
"""

from rest_framework import generics, authentication, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from .serializers import (
    UserSerializer,
    AuthTokenSerializer,
)


class UserRegistrationView(generics.CreateAPIView):
    """Create a new user in the system."""
    serializer_class = UserSerializer


class UserLoginView(ObtainAuthToken):
    """Create a new auth token for user."""
    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


@api_view(['GET'])
def health_check(request):
    """Returns successful response."""
    return Response({'healthy': True})