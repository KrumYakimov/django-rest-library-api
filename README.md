# Library API
A simple API for managing a library of books using the Django REST framework. It was developed as part of a Django REST for the Django Advanced course at Software University.

## Features
- Full CRUD (Create, Read, Update, Delete) functionality for books.
- Responsive frontend interface integrated with JavaScript for real-time interactions.
- Comprehensive API documentation with Swagger UI and ReDoc.
- Backend powered by Django REST Framework.

## Core Functionality
### Books Management
- **Endpoints**:
  - `GET /api/books/`: Retrieve a list of all books.
  - `POST /api/books/`: Create a new book.
  - `GET /api/books/<id>/`: Retrieve details of a specific book by ID.
  - `PUT /api/books/<id>/`: Update an existing book by ID.
  - `DELETE /api/books/<id>/`: Delete a specific book by ID.
- **Interactive Frontend**:
  - Create, retrieve, update, and delete books using an integrated HTML and JavaScript interface.
  - Real-time updates and communication with the API using JavaScript.

### API Documentation
- Schema generated using [drf-spectacular](https://github.com/tfranzel/drf-spectacular).
- Available at:
  - Swagger UI: [http://127.0.0.1:8000/api/schema/swagger-ui/](http://127.0.0.1:8000/api/schema/swagger-ui/)
  - ReDoc: [http://127.0.0.1:8000/api/schema/redoc/](http://127.0.0.1:8000/api/schema/redoc/)

---

## Installation Instructions

### Prerequisites
- Python 3.11 or higher.
- PostgreSQL or SQLite (for database support).

### Steps to Set Up

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. **Set Up a Virtual Environment**:
   - For macOS/Linux:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```
   - For Windows:
     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up the Database**:
   - Create a PostgreSQL database:
     ```sql
     CREATE DATABASE <database_name>;
     ```
   - Add your database credentials to the `.env` file:
     ```plaintext
     SECRET_KEY=<your_django_secret_key>
     DB_NAME=<database_name>
     DB_USER=<username>
     DB_PASSWORD=<password>
     DB_HOST=localhost
     DB_PORT=5432
     ```

5. **Run Database Migrations**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Start the Development Server**:
   ```bash
   python manage.py runserver
   ```

---

## Accessing the Application

### Frontend Interface
- Access the interactive frontend for managing books at:  
  [http://127.0.0.1:8000/static/index.html](http://127.0.0.1:8000/static/index.html)

### API Documentation
- Explore the API using:
  - Swagger UI: [http://127.0.0.1:8000/api/schema/swagger-ui/](http://127.0.0.1:8000/api/schema/swagger-ui/)
  - ReDoc: [http://127.0.0.1:8000/api/schema/redoc/](http://127.0.0.1:8000/api/schema/redoc/)

---

## Example Book Object

```json
{
    "id": 1,
    "title": "Django Unleashed",
    "pages": 350,
    "description": "A comprehensive guide to Django development.",
    "author": "Andrew Pinkham",
    "genre": "FI",
    "published_date": "2024-10-01"
}
```

---

## API Endpoints Overview

| Method | Endpoint                  | Description                       |
|--------|---------------------------|-----------------------------------|
| GET    | `/api/books/`             | List all books.                  |
| POST   | `/api/books/`             | Create a new book.               |
| GET    | `/api/books/<id>/`        | Retrieve a specific book by ID.  |
| PUT    | `/api/books/<id>/`        | Update a specific book by ID.    |
| DELETE | `/api/books/<id>/`        | Delete a specific book by ID.    |

---

### Notes on API Schema Integration
The application uses **drf-spectacular** for API schema generation. The schema is available at:
- **Swagger UI**: [http://127.0.0.1:8000/api/schema/swagger-ui/](http://127.0.0.1:8000/api/schema/swagger-ui/)
- **ReDoc**: [http://127.0.0.1:8000/api/schema/redoc/](http://127.0.0.1:8000/api/schema/redoc/)

---