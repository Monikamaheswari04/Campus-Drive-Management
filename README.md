# Campus-Drive-Management

🌟 Campus Drive Management System

Campus Drive Management System — A clean and modern Django-based campus recruitment portal that displays company drives, allows student registrations with resume uploads, and provides full admin control for managing drives, users, and media files. Built with Django 5.x, Bootstrap, SQLite, and Pillow.
📌 Table of Contents

Project Overview

Tech Stack

Features

Project Structure

Quick Setup — Run Locally

Database & Media Handling

Django Admin Access

requirements.txt

License

📘 Project Overview

CAMPUS Drive is a Django web application designed to streamline campus recruitment by displaying company drives (from the Companyinfo model) and allowing students to apply using a simple registration form (Register model).

The project includes:

Login & Sign-up pages

Company listing with images

Resume upload

Django admin integration

Static + media handling configured

🛠 Tech Stack
Component	Technology
Language	Python 3.9+
Framework	Django 5.x (built using Django 5.0.2)
Frontend	HTML, CSS, Bootstrap CDN
Database	SQLite
Media Handling	Pillow
✨ Features

✔️ Clean landing page with company cards (logo, position, description)
✔️ User Sign-up & Login
✔️ Apply/Register page with resume upload
✔️ Django admin panel for managing companies & users
✔️ Static & Media configuration included
✔️ Fully extendable for authentication, dashboards, or API integration

📂 Project Structure
campus/
├─ manage.py
├─ myproject/
│  ├─ settings.py
│  ├─ urls.py
│  ├─ wsgi.py
│  └─ asgi.py
├─ myapp/
│  ├─ admin.py
│  ├─ models.py
│  ├─ views.py
│  ├─ urls.py
│  └─ apps.py
├─ templates/
│  ├─ index.html
│  ├─ home.html
│  ├─ login.html
│  ├─ register.html
│  ├─ signup.html
│  └─ success.html
├─ static/
│  └─ images/
├─ media/
└─ db.sqlite3

🚀 Quick Setup — Run Locally
1️⃣ Clone the repository
git clone <your-repo-url>
cd campus

2️⃣ Create & activate virtual environment
python -m venv venv


Windows

venv\Scripts\activate


macOS/Linux

source venv/bin/activate

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Run migrations
python manage.py makemigrations
python manage.py migrate

5️⃣ Optional: Create an admin user
python manage.py createsuperuser

6️⃣ Start development server
python manage.py runserver

🗂 Database & Media Handling

✔ Uses SQLite as the default DB
✔ Media files configured with:

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'


✔ Supports company images & resume uploads

🔑 Django Admin Access

Your myapp/admin.py registers:

Userdata

Companyinfo

From Django Admin, you can:

Add/update company recruitment drives

Upload company logos

Manage user registrations

Access:

http://127.0.0.1:8000/admin/

📄 Recommended requirements.txt
Django==5.0.2
Pillow>=10.0.0

📝 License & Contact

This project can be used freely for learning, academic purposes, or extended for your own projects.

Recommended License: MIT License



