# Biblios - Book Reading Tracker

A personal book reading tracker application that helps users manage their reading journey with features for book management, progress tracking, and reading statistics visualization.

## 🚀 Features

-   **User Authentication**: Secure registration, login, and logout functionality
-   **Book Management**: Complete CRUD operations for managing your book library
-   **Reading Progress Tracking**: Track current page and calculate reading progress
-   **Status Management**: Organize books as "Want to Read", "Reading", or "Finished"
-   **Genre Categorization**: Classify books by genre (Fiction, Non-Fiction, Mystery, etc.)
-   **Cover Images**: Upload and display book cover images
-   **Reading Statistics**: Visual dashboard with charts showing reading habits
-   **Responsive Design**: Mobile-friendly interface that works on all devices
-   **Admin Panel**: Django admin interface for data management

## 🛠️ Tech Stack

### Backend

-   **Django 5.2.5** - Python web framework
-   **Django REST Framework** - API development
-   **SQLite** - Database (development)
-   **JWT Authentication** - Secure token-based auth
-   **Pillow** - Image processing for book covers
-   **django-cors-headers** - CORS handling for frontend integration

### Frontend (To be implemented)

-   **React with TypeScript** - Modern frontend framework
-   **Ant Design** - UI component library
-   **Chart.js** - Data visualization
-   **Axios** - HTTP client for API calls
-   **JSON Server** - Mock data for genres

## 📁 Project Structure

```
biblios_bhatiyani/
├── backend/
│   ├── biblios/              # Django project configuration
│   │   ├── settings.py       # Project settings
│   │   ├── urls.py          # Main URL configuration
│   │   └── wsgi.py          # WSGI configuration
│   ├── accounts/            # User management app
│   │   ├── models.py        # Custom User model
│   │   ├── admin.py         # User admin interface
│   │   └── api/            # API views and serializers
│   ├── books/              # Book management app
│   │   ├── models.py       # Book model
│   │   ├── admin.py        # Book admin interface
│   │   └── api/           # API views and serializers
│   ├── stats/             # Statistics app
│   │   └── api/          # Statistics endpoints
│   ├── media/            # User uploaded files
│   ├── static/           # Static files
│   ├── db.json           # JSON Server data
│   ├── manage.py         # Django management script
│   └── requirements.txt  # Python dependencies
├── frontend/             # React frontend (to be created)
├── README.md            # Project documentation
└── prompts.md          # AI usage documentation
```

## 🚀 Getting Started

### Prerequisites

-   Python 3.8+
-   pip (Python package manager)
-   Node.js and npm (for frontend, when implemented)
-   Git

### Backend Setup

1. **Clone the repository**

    ```bash
    git clone https://github.com/yourusername/biblios_bhatiyani.git
    cd biblios_bhatiyani
    ```

2. **Navigate to backend directory**

    ```bash
    cd backend
    ```

3. **Create and activate virtual environment**

    ```bash
    # Create virtual environment
    python -m venv venv

    # Activate virtual environment
    # On Windows:
    venv\Scripts\activate
    # On Mac/Linux:
    source venv/bin/activate
    ```

4. **Install dependencies**

    ```bash
    pip install -r requirements.txt
    ```

5. **Set up environment variables**

    ```bash
    # Create .env file in backend directory
    # Add the following:
    SECRET_KEY=your-secret-key-here
    DEBUG=True
    ALLOWED_HOSTS=localhost,127.0.0.1
    ```

6. **Run database migrations**

    ```bash
    python manage.py migrate
    ```

7. **Create a superuser account**

    ```bash
    python manage.py createsuperuser
    # Follow the prompts to create admin account
    ```

8. **Run the development server**

    ```bash
    python manage.py runserver
    ```

9. **Access the application**
    - API: http://127.0.0.1:8000/
    - Admin Panel: http://127.0.0.1:8000/admin/

### Frontend Setup (To be implemented)

```bash
cd frontend
npm install
npm start
```

## 🤝 Contributing

This is a personal assessment project, but feedback and suggestions are welcome!

## 📄 License

MIT License - feel free to use this project as a reference for your own learning.
