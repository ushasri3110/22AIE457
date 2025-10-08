
# 🏡 CommUnity — Seamless Community Interaction and Management
**CommUnity** is a lightweight and modular web application designed to simplify communication and management within residential communities or housing societies.  
It provides an integrated platform for **residents** and **administrators** to interact efficiently through features like complaint tracking,notices, and event management.

## 👤 User Roles
**Admin** - Can manage complaints, post notices, and create community events.

**Resident** - Can raise and track complaints, view notices, and check upcoming events.

## 🛠️ Technologies Used
- **Frontend:** HTML, CSS, Bootstrap 5, jQuery, Jinja2 Templates  
- **Backend:** Flask (Python)  
- **Database:** SQLite
- **Authentication:** Flask Session Management

## ⚙️ Setup Instructions
-  **Clone the Repository** - git clone https://github.com/ushasri3110/22AIE457
- **Install Dependencies** - pip install -r requirements.txt
- **Run app.py** - python app.py

## 🌐 End Points

- 🏠 Home page of the application - /

![Home Page Screenshot](https://i.ibb.co/jPQ4FJ3y/Screenshot-2025-10-08-101405.png)

- 🔐 User login page - /login

![Login Page Screenshot](https://i.ibb.co/214xCdn2/Screenshot-2025-10-08-102055.png)

- 📝 User registration page - /signup

![Signup Page Screenshot](https://i.ibb.co/zWxcnn5z/Screenshot-2025-10-08-104303.png)

- 📊 User dashboard - /dashboard

![Dashboard Screenshot](https://i.ibb.co/7FsLy4J/Screenshot-2025-10-08-103221.png)

- 🗣️ Residents can post complaints; admins can view and close /complaints - /complaints

Admin

![Admin Complaints Page Screenshot](https://i.ibb.co/dsNRJgVq/Screenshot-2025-10-08-105130.png)

Resident

![Resident Complaints Page Screenshot](https://i.ibb.co/DfwSZxYY/Screenshot-2025-10-08-105026.png)

- 📢 Admins can post notices; residents can view them - /notices

Admin

![Admin Notices Page Screenshot](https://i.ibb.co/8Vyyc34/Screenshot-2025-10-08-103359.png)

Resident

![Resident Notices Page Screenshot](https://i.ibb.co/3yRBXmFs/Screenshot-2025-10-08-104701.png)

- 🎉 Admins can post events; residents can view - /events

Admin

![Admin Events Page Screenshot](https://i.ibb.co/TMLyVD2b/Screenshot-2025-10-08-103922.png)

Resident

![Resident Events Page Screenshot](https://i.ibb.co/G1BjdqQ/Screenshot-2025-10-08-104834.png)
