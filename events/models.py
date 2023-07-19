
"""events/models.py
"""

from django.db import models
from userManager.models import User
from django.conf import settings

class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    event_date = models.DateField(auto_now_add=False)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='owned_events')
    participants = models.ManyToManyField(User, through='EventRegistration', related_name='events_participating')

    def __str__(self):
        return self.title

class EventRegistration(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    joined_at = models.DateTimeField(auto_now_add=True)
    is_attending = models.BooleanField(default=False)

    class Meta:
        unique_together = ('user', 'event') 

    
