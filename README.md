# BackendEngineerAssesment

## Requirements
This Repository an "events" web application where users can log in, create events and sign up for an event and withdraw from an event. This is for demonstrations of the skills in Python Django Framework. Any user can list events:
● Sorted so that upcoming events are first.
● List view shows title, date and amount of participants.
● List view shows the owner of the event (as the part of the email before the "@").
● Assume there will be many thousands of events, users and participants per event.


## EventManager
Event manager APi is rest api develop using django and django rest framework. Following are the complete steps to run and understands the Event Manager API.

## Components:
The is developed in Django and Django Rest Framework and data source is sqlite db which comes in default. Following are the some of components of the Project.
1. UserManager: The API which allow user to login and register into the api. Following are the methods allow by user api
   ```POST  /api/user/login/```
   ```POST /api/user/register/```
   
3. Events: The Api responsible for event management. There are two endpoints in this API and these are:
   ```events endpoint
     GET /api/events/
     POST /api/events/
     GET /api/events/{id}/
     PUT /api/events/{id}/
     PATCH /api/events/{id}/
     DELETE /api/events/{id}/
   ```
   Only the current authenticated user can see all his events which he has created not the others' users event

   ```event-register
     GET /api/events/
     POST /api/events/
     PATCH /api/events/{id}/
     DELETE /api/events/{id}/
   ```
   
   The `GET` will return the list of all users' events. Through `POST` request and a user can register for an event. Through `PUT` withdraw himself from event. `DELETE` will delete the entry from the from the database. `GET` and `PUT` are not allowed will return an error.
4. Other Components includes:
     - drf-spectacular for api documentation, endpoint for is `/api/docs/` and `/api/schema/`
     - rest_framework.authtoken for token authentication.

## Project Setup
Following are the steps for project setup:
1. settup virtual environment. First install, create and activate virtual environment.
   ```
   pip install venv
   python -m venv somename
   somename\sources\activate
   ```
2. Install the requirement from requirements.txt file.
   ```
   pip install -r requirements.txt
   ```
3. Make migrations and migrate
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```
4. Lastly run the server on local premises using command
   ```
   python manage.py runserver
   ```

