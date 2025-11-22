Campus Drive Management System
A clean and modern Django-based campus recruitment portal that displays company drives, allows student registrations with resume uploads, and provides complete admin control. Built using Django 5.x, Bootstrap, SQLite, and Pillow.

📘 Project Overview
The Campus Drive Management System helps streamline campus recruitment by displaying company drives and allowing students to apply with resume uploads. It includes authentication, Django admin integration, media handling, and extendable modular structure.

🛠 Tech Stack
• **Language:** Python 3.9+
• **Framework:** Django 5.x (5.0.2)
• **Frontend:** HTML, CSS, Bootstrap
• **Database:** SQLite
• **Media:** Pillow

✨ Features
✔️ Clean landing page with company cards
✔️ User Sign-up & Login
✔️ Resume upload functionality
✔️ Django admin integration
✔️ Static & media configuration included
✔️ Fully extendable for future features

📂 Professional Project Structure
campus/
│── manage.py
│── db.sqlite3
│── requirements.txt
│── media/
│── static/
│    └── images/
│
├── myproject/
│    ├── __init__.py
│    ├── settings.py
│    ├── urls.py
│    ├── asgi.py
│    └── wsgi.py
│
└── myapp/
     ├── __init__.py
     ├── admin.py
     ├── models.py
     ├── views.py
     ├── urls.py
     ├── forms.py
     └── templates/
           ├── index.html
           ├── login.html
           ├── signup.html
           ├── register.html
           └── success.html

🚀 Quick Setup
1️⃣ Clone the repository
   git clone <repo-url>

2️⃣ Create virtual environment
   python -m venv venv

3️⃣ Install dependencies
   pip install -r requirements.txt

4️⃣ Run migrations
   python manage.py migrate

5️⃣ Start server
   python manage.py runserver

📝 License
Recommended: MIT License

