from django.test import TestCase
from userManager.models import User
from rest_framework.test import APIRequestFactory, force_authenticate
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Event, EventRegistration
from .views import EventViewSet, EventRegistrationViewSet




class EventViewSetAuthenticatedTests(TestCase):
    def setUp(self):
        # Create a test user and an event
        self.user = User.objects.create_user(
            email="user@testmail.com", 
            name='testuser', 
            password='testpass'
        )
        self.event = Event.objects.create(
            title='Test Event', 
            description='This is a test event', 
            owner=self.user, 
            event_date="2023-08-25"
        )
        # Initialize APIRequestFactory
        self.factory = APIRequestFactory()

    def test_list_events_authenticated(self):
        # Create an authenticated request
        request = self.factory.get('/events/')
        force_authenticate(request, user=self.user)

        # Instantiate the EventViewSet and retrieve the list of events
        view = EventViewSet.as_view({'get': 'list'})
        response = view(request)

        # Check the response status code
        self.assertEqual(response.status_code, 200)

        # Check if the event created by the user is prefrom rest_framework.authtoken.models import Tokensent in the response
        self.assertContains(response, 'Test Event')

    def test_retrieve_event_authenticated(self):
        # Create an authenticated request
        request = self.factory.get('/events/{0}/'.format(self.event.id))
        force_authenticate(request, user=self.user)

        # Instantiate the EventViewSet and retrieve a specific event
        view = EventViewSet.as_view({'get': 'retrieve'})
        response = view(request, pk=self.event.id)

        # Check the response status code
        self.assertEqual(response.status_code, 200)

        # Check if the event's title is present in the response
        self.assertContains(response, 'Test Event')

    def test_create_event_authenticated(self):
        # Create an authenticated request
        data = {
            'title': 'New Event',
            'description': 'This is a new event.',
            'owner': self.user,
            'event_date':'2023-08-25'
        }
        request = self.factory.post('/events/', data)
        force_authenticate(request, user=self.user)

        # Instantiate the EventViewSet and create a new event
        view = EventViewSet.as_view({'post': 'create'})
        response = view(request)

        # Check the response status code
        self.assertEqual(response.status_code, 201)

        # Check if the event is created successfully
        self.assertEqual(Event.objects.count(), 2)  # Assuming there was only one event created in the setUp
        self.assertEqual(Event.objects.last().title, 'New Event')

    def test_update_event_authenticated(self):
        # Create an authenticated request
        data = {
            'title': 'Updated Event',
            'description': 'This is a new event.',
            'owner': self.user,
            'event_date':'2023-08-25'
        }
        request = self.factory.put('/events/{0}/'.format(self.event.id), data)
        force_authenticate(request, user=self.user)

        # Instantiate the EventViewSet and update the event
        view = EventViewSet.as_view({'put': 'update'})
        response = view(request, pk=self.event.id)

        # Check the response status code
        self.assertEqual(response.status_code, 200)

        # Check if the event has been updated successfully
        self.event.refresh_from_db()
        self.assertEqual(self.event.title, 'Updated Event')

    def test_delete_event_authenticated(self):
        # Create an authenticated request
        request = self.factory.delete('/events/{0}/'.format(self.event.id))
        force_authenticate(request, user=self.user)

        # Instantiate the EventViewSet and delete the event
        view = EventViewSet.as_view({'delete': 'destroy'})
        response = view(request, pk=self.event.id)

        # Check the response status code
        self.assertEqual(response.status_code, 204)

        # Check if the event has been deleted successfully
        self.assertEqual(Event.objects.count(), 0)


class EventRegistrationTestCase(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.user = User.objects.create_user(
            email="user@testmail.com", 
            name='testuser', 
            password='testpass'
        )
        self.event = Event.objects.create(
            title='Test Event', 
            description='This is a test event', 
            owner=self.user, 
            event_date="2023-08-25"
        )

    def test_list_events(self):
        view = EventRegistrationViewSet.as_view({'get': 'list'})
        request = self.factory.get('/event-register/')
        force_authenticate(request, user=self.user)
        response = view(request)
        self.assertEqual(response.status_code, 200)

    def test_create_event_registration(self):
        view = EventRegistrationViewSet.as_view({'post': 'create'})
        data = {'event': self.event.id, 'is_attending': False, 'user':self.user}
        request = self.factory.post('/event-register/', data=data)
        force_authenticate(request, user=self.user)
        response = view(request)
        self.assertEqual(response.status_code, 201)

    def test_destroy_event_registration(self):
        registration = EventRegistration.objects.create(event=self.event, user=self.user, is_attending=True)
        view = EventRegistrationViewSet.as_view({'delete': 'destroy'})
        request = self.factory.delete(f'/event-register/{registration.id}/')
        force_authenticate(request, user=self.user)
        response = view(request, pk=registration.id)
        self.assertEqual(response.status_code, 204)

    

