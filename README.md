# Django Food App 🍔

A full-stack web application built with **Python** and **Django** for dynamic food menu management and ordering. This project demonstrates clean architecture, robust CRUD operations, and a seamless user interface.

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Django](https://img.shields.io/badge/Django-4.x-green.svg)](https://www.djangoproject.com/)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

## 🚀 Key Features

* **Menu Management:** Full CRUD (Create, Read, Update, Delete) capabilities for food items
* **Dynamic Routing:** Structured URL handling for menu details and categories
* **Admin Dashboard:** Secure interface for restaurant owners to manage listings without code
* **Responsive Design:** Fully mobile-friendly UI for browsing on any device
* **ORM Integration:** Efficient database queries using Django's Object-Relational Mapper
* **Search & Filter:** Quick search functionality to find food items
* **User Authentication:** Secure login system for customers and administrators

## 🛠️ Tech Stack

* **Backend:** Python 3.x, Django 4.x
* **Frontend:** HTML5, CSS3, JavaScript, Bootstrap 5
* **Database:** SQLite (Development) / PostgreSQL (Production)
* **Tools:** Git, Virtualenv, Pip

## 📁 Project Structure

```text
Django-Food-App/
├── FoodApp/            # Project configuration
│   ├── settings.py     # Django settings
│   ├── urls.py         # Root URL configuration
│   ├── wsgi.py         # WSGI application
│   └── asgi.py         # ASGI application
├── Food/               # Main application
│   ├── migrations/     # Database schema history
│   ├── templates/      # HTML frontend files
│   ├── static/         # App-specific static files
│   ├── models.py       # Data models for food items
│   ├── views.py        # View logic
│   ├── urls.py         # App URL routing
│   ├── admin.py        # Admin interface config
│   └── forms.py        # Form definitions
├── static/             # Global CSS, Images, and JS assets
├── media/              # User-uploaded content
├── manage.py           # Django command-line utility
├── requirements.txt    # Project dependencies
├── .gitignore          # Git ignore rules
└── README.md           # Project documentation
```

---

## 🍴 Installation Guide

Follow these steps to set up the **Django Food App** on your local machine.

### 🛠️ Prerequisites

Before beginning, ensure you have the following installed:

* **Python 3.10+**: [Download here](https://www.python.org/downloads/)
* **Git**: [Download here](https://git-scm.com/)
* **Pip**: Usually comes bundled with Python installations

Verify your installations:

```bash
python --version
git --version
pip --version
```

---

### 📥 Step 1: Clone the Repository

Clone the project from GitHub and navigate into the project directory:

```bash
git clone https://github.com/Harshgupta88156/Django-Food-App.git
cd Django-Food-App
```

---

### 🐍 Step 2: Create a Virtual Environment

Creating a virtual environment isolates your project dependencies from other Python projects.

**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**On macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

You should see `(venv)` appear in your terminal prompt, indicating the virtual environment is active.

---

### 📦 Step 3: Install Dependencies

Install all required Python packages using the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

If `requirements.txt` is missing, install Django manually:

```bash
pip install django pillow
```

---

### 🗄️ Step 4: Set Up the Database

Run migrations to create the database schema:

```bash
python manage.py makemigrations
python manage.py migrate
```

This will create an SQLite database file (`db.sqlite3`) in your project root.

---

### 👤 Step 5: Create a Superuser

Create an admin account to access the Django admin panel:

```bash
python manage.py createsuperuser
```

You'll be prompted to enter:
* Username
* Email address (optional)
* Password (enter twice for confirmation)

---

### 📂 Step 6: Collect Static Files

Gather all static files into one directory:

```bash
python manage.py collectstatic
```

Type `yes` when prompted.

---

### 🚀 Step 7: Run the Development Server

Start the Django development server:

```bash
python manage.py runserver
```

You should see output like:

```
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```

---

### 🌐 Step 8: Access the Application

Open your web browser and navigate to:

* **Main Application:** [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
* **Admin Panel:** [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

Log in to the admin panel using the superuser credentials you created in Step 5.

---

## 🎯 Usage

### Adding Food Items

1. Navigate to the admin panel at `/admin/`
2. Click on **Food items** under the Food section
3. Click **Add Food Item**
4. Fill in the details (name, description, price, image, etc.)
5. Click **Save**

### Managing Categories

1. In the admin panel, go to **Categories**
2. Add, edit, or delete food categories
3. Assign food items to categories for better organization

### Customer Ordering

1. Browse the menu on the homepage
2. Use search and filters to find items
3. View item details by clicking on food cards
4. Add items to cart and proceed to checkout

---

## 🔧 Configuration

### Environment Variables (Optional)

For production deployments, create a `.env` file in the project root:

```env
SECRET_KEY=your-secret-key-here
DEBUG=False
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
DATABASE_URL=postgresql://user:password@localhost/dbname
```

### Database Configuration

To switch from SQLite to PostgreSQL for production:

1. Install PostgreSQL and create a database
2. Install `psycopg2`: `pip install psycopg2-binary`
3. Update `settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

---

## 🧪 Running Tests

Run the test suite to ensure everything works correctly:

```bash
python manage.py test
```

---

## 🐛 Troubleshooting

### Common Issues

**Issue:** `ModuleNotFoundError: No module named 'django'`
**Solution:** Ensure your virtual environment is activated and Django is installed:
```bash
pip install django
```

**Issue:** Port 8000 is already in use
**Solution:** Run the server on a different port:
```bash
python manage.py runserver 8080
```

**Issue:** Static files not loading
**Solution:** Run `collectstatic` and check your `STATIC_URL` settings:
```bash
python manage.py collectstatic
```

**Issue:** Database errors after pulling updates
**Solution:** Run migrations:
```bash
python manage.py migrate
```

---

## 📝 Development Workflow

1. **Create a new branch** for your feature:
   ```bash
   git checkout -b feature-name
   ```

2. **Make your changes** and test thoroughly

3. **Commit your changes**:
   ```bash
   git add .
   git commit -m "Description of changes"
   ```

4. **Push to GitHub**:
   ```bash
   git push origin feature-name
   ```

5. **Create a Pull Request** on GitHub

---

## 🚀 Deployment

### Deploying to Heroku

1. Install Heroku CLI
2. Create a `Procfile`:
   ```
   web: gunicorn FoodApp.wsgi
   ```
3. Install gunicorn: `pip install gunicorn`
4. Update `requirements.txt`: `pip freeze > requirements.txt`
5. Deploy:
   ```bash
   heroku login
   heroku create your-app-name
   git push heroku main
   heroku run python manage.py migrate
   heroku run python manage.py createsuperuser
   ```

### Deploying to AWS/DigitalOcean

Follow Django's deployment checklist and configure:
- Static files serving (use WhiteNoise or S3)
- Database (RDS or managed PostgreSQL)
- Security settings (HTTPS, CSRF, CORS)
- Environment variables

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

**Harsh Gupta**

* GitHub: [@Harshgupta88156](https://github.com/Harshgupta88156)
* Repository: [Django-Food-App](https://github.com/Harshgupta88156/Django-Food-App)

---

## 🙏 Acknowledgments

* Django Documentation
* Bootstrap Framework
* Python Community
* All contributors and supporters

---

## 📧 Contact & Support

If you have questions or need help:

* Open an issue on GitHub
* Check existing issues for solutions
* Contact the maintainer through GitHub

---

**⭐ If you find this project useful, please consider giving it a star on GitHub!**
