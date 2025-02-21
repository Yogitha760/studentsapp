projectname:studentsapp
appname:allnotes

# 1. Check Python Version
python --version

# 2. Check Pip Version
pip --version

# 3. Install Python (If Not Installed) - Use Official Website  
# 4. Install Pip (If Not Installed) - Comes with Python by Default  

# 5. Create Virtual Environment
python -m venv pyenv

# 6. Activate Virtual Environment
pyenv\Scripts\activate  # Windows
source pyenv/bin/activate  # Mac/Linux

# 7. Install Django
pip install django

# 8. Create Django Project
django-admin startproject studentsapp

# 9. Navigate to Project Directory
cd studentsapp

# 10. Run Django Development Server
python manage.py runserver

# 11. Create Django App
python manage.py startapp allnotes

# 12. Register App in Installed Apps (Add 'allnotes' to INSTALLED_APPS in settings.py) from studentsapp/settings.py

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'allnotes',  # Add this line
]



# 13. Modify models.py (Define Database Schema)

# 14. Apply Migrations
python manage.py makemigrations allnotes
python manage.py migrate

# 15. Register Model in Django Admin
# 16. Create Superuser for Admin Panel
python manage.py createsuperuser

# 17. Run Server Again
python manage.py runserver

# 18. Modify forms.py (Create Forms for Model)

# 19. Implement CRUD Operations in views.py

# 20. Configure URLs in urls.py (Connect Views to Routes)

# 21. Create HTML Templates in allnotes/templates/allnotes/
save file.htmlnwhich you has to be created.

# 22. Access the Application in Browser  
# Add Note Page: http://127.0.0.1:8000/add/  
# View Notes Page: http://127.0.0.1:8000/list/  
# Admin Panel: http://127.0.0.1:8000/admin/