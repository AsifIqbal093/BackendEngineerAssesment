"""events/serializers.py"""

from rest_framework import serializers
from .models import Event, EventRegistration
from userManager.models import User

class EventSerializer(serializers.ModelSerializer):
    owner = serializers.SerializerMethodField()

    class Meta:
        model = Event
        fields = ('id', 'title', 'description', 'event_date', 'owner', 'participants')
    
    def get_owner(self, obj):
        return obj.owner.email.split('@')[0]
    
    def create(self, validated_data):
        # Map the currently authenticated user to the owner field of the Event model
        user = self.context['request'].user
        validated_data['owner'] = user

        # Create and return the Event instance
        return super().create(validated_data)

class EventRegistrationSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = EventRegistration
        fields = '__all__'
    
