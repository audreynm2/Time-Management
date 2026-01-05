# Time Management API - Capstone Submission

## Overview
A fully functional Task Management API built with Django and Django REST Framework. It features secure JWT authentication, strict task ownership, and advanced filtering.

## 🚀 Key Features & Requirements Met
- **CRUD Operations**: Full support for Tasks and Users via REST endpoints.
- **Task Ownership**: Middleware and queryset filtering ensure users only see their own data.
- **Task Controls**: Dedicated endpoints for marking completion with automated timestamps.
- **Validation**: Strict model-level validation for due dates (future-only) and immutable completed tasks.
- **Filtering & Sorting**: Integrated `django-filter` for status, priority, and date-based queries.
- **Security**: JWT authentication for all protected endpoints.

## 🔌 Quick Demo Access
- **Status Check**: `GET /`
- **Admin Panel**: `/admin/` (User: `admin`, Pass: `admin123`)
- **API Root**: `/api/tasks/`

## 🛠️ Architecture
- **API Layer**: DRF ViewSets for modular logic.
- **Model Layer**: Django ORM with custom `clean()` and `save()` overrides for business logic.
- **Auth Layer**: JWT using `rest_framework_simplejwt`.

## 📦 Deployment
- Configured for Replit Autoscale.
- Ready for PythonAnywhere/Heroku deployment.
