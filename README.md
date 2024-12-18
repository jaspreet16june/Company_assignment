This Django application provides a system for managing companies and users with custom authentication using email/password instead of the default username. The application includes:

Login/Logout functionality.
Detail pages for Users and Companies behind authentication.
Users can edit their own details.
CRUD APIs for both Company and User models via Django REST Framework (DRF).

Features
Custom User Model: Authentication via email/password.
Company Model: Manage company details like name, address, and website.
Login/Logout: Built-in login/logout functionality.
Detail Pages: Users can view and edit their details; companies have a detail page.
CRUD APIs: Expose CRUD operations for both users and companies.

Installation::
1. Clone the repository:
   git clone https://github.com/yourusername/django-company-user-app.git
   cd Company_assignment

2. Create a virtual environment:
   Virtualenv venv
   source venv/bin/activate 

3. Install dependencies:
   pip install -r requirements.txt


Endpoints::
1. Authentication
    Login: /login/
    Logout: /logout/
2. Detail Pages
    User Detail: /user/
    Company Detail: /company/


