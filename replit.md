# Time Management API

## Overview
A Django REST API for task management with JWT authentication. Users can create, manage, and track tasks with priorities, due dates, and completion status.

## Project Structure
- `api/` - Main API application with Task model, serializers, and views
- `project_config/` - Django project settings and URL configuration
- `manage.py` - Django management script

## Tech Stack
- Python 3.11
- Django 5.2
- Django REST Framework
- djangorestframework-simplejwt for JWT authentication
- django-filter for filtering tasks
- SQLite database (development)

## API Endpoints
- `GET /` - API status check
- `POST /api/token/` - Obtain JWT token
- `POST /api/token/refresh/` - Refresh JWT token
- `GET /api/tasks/` - List user tasks
- `POST /api/tasks/` - Create task
- `GET /api/tasks/{id}/` - Get task details
- `PUT /api/tasks/{id}/` - Update task
- `DELETE /api/tasks/{id}/` - Delete task
- `POST /api/tasks/{id}/complete/` - Mark task complete
- `POST /api/tasks/{id}/incomplete/` - Mark task incomplete
- `/admin/` - Django admin interface

## Running Locally
```bash
python manage.py runserver 0.0.0.0:5000
```

## Configuration
- All hosts are allowed for development
- CSRF trusted origins configured for Replit domains
