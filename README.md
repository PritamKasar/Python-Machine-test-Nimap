
# nimap_machineTest

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

## 1. How to Run the Machine

1. Make sure you have **Python 3.13** installed.
2. Install required packages:
    ```bash
    pip install -r requirements.txt
    ```
3. Navigate to the project folder:
    ```bash
    cd nimap_machineTest
    ```
4. Run the Django development server:
    ```bash
    python manage.py runserver
    ```
5. Open your browser and go to:
    ```
    http://127.0.0.1:8000/
    ```

---

## 2. How to Run DB Design

1. Make sure PostgreSQL is installed and running.
2. Create a database:
    ```sql
    CREATE DATABASE nimap_taskdb;
    ```
3. Update your `settings.py` with your database credentials.
4. Apply migrations to set up the tables:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

---

## 3. How to Run the Code

1. Create a superuser to access Django admin:
    ```bash
    python manage.py createsuperuser
    ```
2. Start the development server:
    ```bash
    python manage.py runserver
    ```
3. Use Postman or any API client to test the endpoints:
    - **List projects assigned to logged-in user:**
        ```
        GET /projects/
        ```
    - **Create new project for a client:**
        ```
        POST /clients/:id/projects/
        ```
        Example payload:
        ```json
        {
            "project_name": "Project A",
            "users": [
                {
                    "id": 1,
                    "name": "Rohit"
                }
            ]
        }
        ```
4. Access the admin panel to manage users, projects, and clients:
    ```
    http://127.0.0.1:8000/admin/
    ```

---

