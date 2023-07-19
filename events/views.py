"""events/views.py"""

from rest_framework import  viewsets, status
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Event, EventRegistration
from .serializers import EventSerializer, EventRegistrationSerializer

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all().order_by('event_date')
    serializer_class = EventSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Retrieve the authenticated user from the request
        user = self.request.user

        # Filter the queryset based on the user
        queryset = Event.objects.filter(owner=user)
        return queryset

class EventRegistrationViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventRegistrationSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.action == 'list':
            return Event.objects.all()
        elif self.action in  ['create', 'destroy', 'partial_update']:
            return EventRegistration.objects.filter(user=self.request.user)
        else:
            return None

    def get_serializer_class(self):
        if self.action == 'list':
            return EventSerializer
        elif self.action in  ['create', 'destroy', 'partial_update']:
            return EventRegistrationSerializer
        else:
            return None
    
    # Override the create() method to remove the create method
    def get(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
    
    def update(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

