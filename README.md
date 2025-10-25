# Discussion Board

A Django-based discussion board application where users can create topics and engage in conversations within different boards.

## 📋 Project Overview

This is a web-based discussion forum built with Django 5.2.7 that allows users to participate in topic-based discussions organized by different boards. The application follows Django's MVT (Model-View-Template) architecture pattern.

## ✨ Features

- **Board Management**: Browse multiple discussion boards with descriptions
- **Topic Creation**: Create new topics within specific boards
- **User Authentication**: User signup and login functionality
- **Post System**: Create posts within topics
- **Responsive UI**: Bootstrap 5 integration for modern, responsive design
- **Form Validation**: Client-side and server-side form validation with visual feedback

## 🏗️ Project Structure

```
Discussion Board/
├── manage.py                    # Django management script
├── README.md                    # Project documentation
├── Explain.txt                  # MVT architecture explanation
│
├── Discussion_board/            # Main project configuration
│   ├── __init__.py
│   ├── settings.py             # Project settings and configuration
│   ├── urls.py                 # Main URL routing
│   ├── wsgi.py                 # WSGI configuration
│   └── asgi.py                 # ASGI configuration
│
├── boards/                      # Discussion boards app
│   ├── models.py               # Board, Topic, and Post models
│   ├── views.py                # Business logic for boards
│   ├── forms.py                # NewTopicForm for creating topics
│   ├── url.py                  # Board-specific URL patterns
│   ├── admin.py                # Admin panel configuration
│   └── migrations/             # Database migrations
│
├── accounts/                    # User authentication app
│   ├── views.py                # User signup view
│   ├── url.py                  # Account-related URL patterns
│   └── migrations/             # Database migrations
│
├── templates/                   # HTML templates
│   ├── base.html               # Base template with navbar
│   ├── home.html               # Board listing page
│   ├── topics.html             # Topics within a board
│   ├── new_topic.html          # Create new topic form
│   ├── signup.html             # User registration form
│   └── includes/
│       └── form.html           # Reusable form rendering template
│
└── Static/                      # Static assets
    ├── css/                    # Bootstrap CSS files
    └── js/                     # Bootstrap JavaScript files
```

## 🗄️ Database Schema

### Models

**Board**

- `name`: CharField (max 30 characters, unique)
- `description`: CharField (max 180 characters)

**Topic**

- `subject`: CharField (max 250 characters)
- `board`: ForeignKey to Board (one-to-many)
- `created_by`: ForeignKey to User (one-to-one)
- `created_dt`: DateTimeField (auto-generated)

**Post**

- `message`: TextField (max 4000 characters)
- `topic`: ForeignKey to Topic (one-to-many)
- `created_by`: ForeignKey to User (one-to-many)
- `create_dt`: DateTimeField (auto-generated)

## 🛠️ Technologies Used

- **Backend**: Django 5.2.7 (Python web framework)
- **Database**: PostgreSQL
- **Frontend**: Bootstrap 5 (CSS framework)
- **Form Enhancement**: django-widget-tweaks
- **Template Engine**: Django Template Language

## 📦 Dependencies

- Django 5.2.7
- PostgreSQL (psycopg2)
- django-widget-tweaks (for form styling)

## ⚙️ Configuration

### Database Settings

The application uses PostgreSQL with the following default configuration:

- **Database Name**: Dissussion_Board
- **User**: postgres
- **Host**: localhost
- **Port**: 5432

### Static Files

- Static files are served from the `Static/` directory
- Bootstrap 5 CSS and JavaScript are included

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- PostgreSQL database
- pip (Python package manager)

### Installation

1. Clone the repository

```bash
git clone <repository-url>
cd Discussion_board
```

2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies

```bash
pip install django psycopg2 django-widget-tweaks
```

4. Configure database

- Create a PostgreSQL database named `Dissussion_Board`
- Update database credentials in `Discussion_board/settings.py` if needed

5. Run migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

6. Create a superuser (optional)

```bash
python manage.py createsuperuser
```

7. Run the development server

```bash
python manage.py runserver
```

8. Access the application at `http://127.0.0.1:8000/`

## 🔗 URL Routes

- `/` - Home page (list of boards)
- `/about/` - About page
- `/boards/<board_id>/` - Topics within a specific board
- `/boards/<board_id>/new/` - Create a new topic in a board
- `/signup/` - User registration
- `/admin/` - Django admin panel

## 🎨 User Interface

The application uses Bootstrap 5 for a clean, responsive design featuring:

- Dark navigation bar with authentication status
- Breadcrumb navigation for easy traversal
- Table-based layouts for boards and topics
- Form validation with visual feedback (valid/invalid states)
- Responsive design for mobile and desktop

## 🔐 Security Notes

⚠️ **Important**: Before deploying to production:

1. Change the `SECRET_KEY` in settings.py
2. Set `DEBUG = False`
3. Configure `ALLOWED_HOSTS`
4. Use environment variables for sensitive data
5. Set up proper database credentials

## 📝 MVT Architecture

This project follows Django's MVT (Model-View-Template) pattern:

- **Model**: Defines data structure (Board, Topic, Post)
- **View**: Contains business logic and handles requests
- **Template**: Renders the UI with dynamic content

See `Explain.txt` for a detailed explanation of the MVT architecture.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 👤 Author

Amera Mahmoud

## 🔮 Future Enhancements

- User authentication completion (login/logout)
- Reply to posts functionality
- User profiles and avatars
- Post editing and deletion
- Search functionality
- Pagination for topics and posts
- Markdown support for posts
- Email notifications
- User reputation system
