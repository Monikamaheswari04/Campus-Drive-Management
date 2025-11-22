# Campus-Drive-Management

⭐ CAMPUS Drive

A simple Django-based campus recruitment portal that displays company drives and allows students to view company details and apply/register for positions. This repository contains templates, models, URL routing, and basic static/media handling — ready to run locally and extend.

📌 Table of Contents

Project Overview

Tech Stack

Features

Project Structure

Quick Setup — Run Locally

Database & Media Handling

Create Admin / Access Django Admin

Recommended requirements.txt

License & Contact

📘 Project Overview

CAMPUS Drive is a minimal Django application that lists company drives (Companyinfo) and lets users register for positions via a registration form (Register).
It includes user sign-up/login templates and basic static + media configuration (images and resumes).

🛠 Tech Stack

Python (3.9+)

Django 5.x (project created with Django 5.0.2)

SQLite (default database)

Bootstrap (via CDN)

Pillow (image handling)

✨ Features

Home / Landing page showing company cards with image, company name, and job position

Sign-up and Login pages

Company Apply flow (registration form with resume upload)

Admin management of companies and users

Media file support (company images, resumes)

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
│  ├─ apps.py
│  ├─ models.py
│  ├─ urls.py
│  ├─ views.py
│  └─ tests.py
├─ templates/
│  ├─ index.html
│  ├─ home.html
│  ├─ login.html
│  ├─ register.html
│  ├─ sign up/singup.html
│  └─ success.html
├─ static/
│  └─ images (cicon.png, campus.png, etc.)
├─ media/
└─ db.sqlite3

🚀 Quick Setup — Run Locally
1️⃣ Clone the repository
git clone <your-repo-url>
cd campus

2️⃣ Create & activate virtual environment
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Apply migrations
python manage.py makemigrations
python manage.py migrate

5️⃣ Create superuser (optional)
python manage.py createsuperuser

6️⃣ Run development server
python manage.py runserver



🗂 Database & Media Handling

Uses SQLite (db.sqlite3)

Media storage is configured with:

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'


Media files (images/resumes) are served correctly during development.

🔑 Create Admin / Access Django Admin

myapp/admin.py registers:

Userdata

Companyinfo

Admin panel allows adding:

Company details

Company image

User entries

📄 Recommended requirements.txt
Django==5.0.2
Pillow>=10.0.0

📝 License & Contact

This project can be used for learning, academic submissions, or extensions.
Add a license of your choice (MIT recommended).

For any queries, feel free to contact.
