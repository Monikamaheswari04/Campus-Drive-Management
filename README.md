🎓 Campus Drive Management System

A clean and modern Django-based Campus Recruitment Portal that displays company drives, allows students to register and upload resumes, and provides complete admin control.
Built using Django 5.x, Bootstrap, SQLite, and Pillow.

📘 Project Overview

The Campus Drive Management System streamlines the campus placement workflow by:

Displaying current company drives

Allowing students to register & upload resumes

Providing a secure authentication system

Offering Django Admin control for managing drives, users, and media

Maintaining a modular, extendable project structure

This project is ideal for college placements, training & placement departments, and Django beginners looking to build real-world applications.

✨ Features Implemented

✔️ Clean & responsive landing page
✔️ Student Signup & Login
✔️ Resume upload (PDF/DOC)
✔️ Company-wise drive registration
✔️ Django Admin Panel for full CRUD operations
✔️ Static & media configuration included
✔️ Modular structure ready for future expansion

🛠 Tech Stack
Category	Technology
Language	Python 3.9+
Framework	Django 5.x (5.0.2)
Frontend	HTML, CSS, Bootstrap
Database	SQLite
Media Handling	Pillow
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

🚀 Setup Instructions
1️⃣ Clone the Repository
git clone <YOUR_REPOSITORY_URL>
cd campus

2️⃣ Create Virtual Environment
python -m venv venv

3️⃣ Activate Virtual Environment

Windows

venv\Scripts\activate


Mac/Linux

source venv/bin/activate

4️⃣ Install Dependencies
pip install -r requirements.txt

5️⃣ Apply Migrations
python manage.py migrate

6️⃣ Run Development Server
python manage.py runserver


Your app is now live at:
👉 http://127.0.0.1:8000/

🎯 Assumptions & Notes

Students must register/login before applying for any drive

Admin manages all drive details through Django Admin Panel

Resume uploads are stored in the media folder

Provided structure is extendable for future modules like:

Placement analytics

Admin dashboards

Drive shortlisting system

🌟 Future Enhancements

🔹 Add Email Notifications for drive registration
🔹 Student Dashboard to view applied drives
🔹 Company HR login module
🔹 REST API integration for mobile apps
🔹 Deployment on AWS/Render/Heroku

📝 License

Recommended License: MIT License

👩‍💻 Author

Monika A.D.
B.Tech Artificial Intelligence & Data Science
November 2025
