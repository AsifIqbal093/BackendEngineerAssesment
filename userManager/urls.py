"""
URL mappings for the user API.
"""

from django.urls import path
from userManager import views


app_name = 'userManager'

urlpatterns = [
    path('register/', views.UserRegistrationView.as_view(), name='user-registration'),
    path('login/', views.UserLoginView.as_view(), name='user-login'),
]