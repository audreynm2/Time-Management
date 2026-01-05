
# 🕒 Time Management API

## 📌 Description

The Time Management API is a Django-based backend service designed to help users manage tasks efficiently. It follows RESTful design principles and provides a robust foundation for productivity applications.

## 🚀 Key Features

* **User Authentication**: Secure JWT-based authentication.
* **Task Management (CRUD)**: Create, Read, Update, and Delete tasks.
* **Task Ownership**: Users can only access and manage their own tasks.
* **Task Controls**: Mark tasks as complete/incomplete with timestamps.
* **Advanced Filtering & Sorting**: Filter by status, priority, and due date. Sort by due date or priority.
* **Validation**: Due dates must be in the future, and completed tasks are locked until marked incomplete.

## 🛠️ Tech Stack

* **Backend**: Django & Django REST Framework
* **Auth**: SimpleJWT
* **Database**: SQLite (Development) / PostgreSQL (Production ready)
* **Tools**: Django Filters

## 🔌 API Endpoints

### Authentication
* `POST /api/token/` - Obtain JWT token (JSON with `username` and `password`)
* `POST /api/token/refresh/` - Refresh expired token

### Tasks
* `GET /api/tasks/` - List user's tasks (Supports `?status=`, `?priority=`, `?ordering=`)
* `POST /api/tasks/` - Create a new task
* `GET /api/tasks/{id}/` - View task details
* `PUT /api/tasks/{id}/` - Update task (Locked if status is 'Completed')
* `DELETE /api/tasks/{id}/` - Remove task
* `POST /api/tasks/{id}/complete/` - Mark as complete
* `POST /api/tasks/{id}/incomplete/` - Mark as incomplete

## 🧱 Setup & Installation

1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`.
3. Run migrations: `python manage.py migrate`.
4. Start server: `python manage.py runserver 0.0.0.0:5000`.

## 👤 Author
**Audrey Machivenyika**
Software Developer

