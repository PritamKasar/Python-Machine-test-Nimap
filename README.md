
# Django Projects API

This Django project provides API endpoints to manage projects and clients. Users can:

- Create projects for clients
- Assign registered users to projects
- List projects assigned to a logged-in user

## Features

- Django REST Framework-based APIs
- User authentication
- Project assignment management

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/PritamKasar/Python-Machine-test-Nimap.git
   cd nimap_machineTest
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Apply migrations:
   ```bash
   python manage.py migrate
   ```
4. Run the development server:
   ```bash
   python manage.py runserver
   ```
5. API Endpoints:

- `GET /projects/` → List projects assigned to the logged-in user
- `POST /clients/:id/projects/` → Create project for a client

## Requirements

- Python 3.10+
- Django 5.x
- Django REST Framework
